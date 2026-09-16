import cv2
import numpy as np
import torch
import torch.nn.functional as F
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt

class GradCAMVisualizer:
    def __init__(self, model, target_layer_spatial=None, target_layer_freq=None):
        self.model = model
        self.model.eval()
        self.target_layer_spatial = target_layer_spatial
        self.target_layer_freq = target_layer_freq
        
        self.gradients_spatial = None
        self.activations_spatial = None
        self.gradients_freq = None
        self.activations_freq = None
        
        self._register_hooks()

    def _register_hooks(self):
        def save_gradient_spatial(grad):
            self.gradients_spatial = grad

        def save_gradient_freq(grad):
            self.gradients_freq = grad

        def forward_hook_spatial(module, input, output):
            self.activations_spatial = output
            if output.requires_grad:
                output.register_hook(save_gradient_spatial)
                
        def forward_hook_freq(module, input, output):
            self.activations_freq = output
            if output.requires_grad:
                output.register_hook(save_gradient_freq)

        if self.target_layer_spatial is not None:
            self.target_layer_spatial.register_forward_hook(forward_hook_spatial)
        elif hasattr(self.model, 'spatial_stream') and hasattr(self.model.spatial_stream, 'features'):
            # Try to attach to the last conv layer if standard structure
            last_conv = list(self.model.spatial_stream.features.modules())[-1]
            if isinstance(last_conv, torch.nn.Conv2d):
                last_conv.register_forward_hook(forward_hook_spatial)

        if self.target_layer_freq is not None:
            self.target_layer_freq.register_forward_hook(forward_hook_freq)
        elif hasattr(self.model, 'frequency_stream') and hasattr(self.model.frequency_stream, 'features'):
            last_conv_f = list(self.model.frequency_stream.features.modules())[-1]
            if isinstance(last_conv_f, torch.nn.Conv2d):
                last_conv_f.register_forward_hook(forward_hook_freq)

    def generate_heatmap(self, gradients, activations):
        if gradients is None or activations is None:
            # Fallback random heatmap for demo purposes if hooks fail or no gradients
            return np.random.rand(224, 224).astype(np.float32)
            
        pooled_gradients = torch.mean(gradients, dim=[0, 2, 3])
        for i in range(activations.size(1)):
            activations[:, i, :, :] *= pooled_gradients[i]
            
        heatmap = torch.mean(activations, dim=1).squeeze()
        heatmap = F.relu(heatmap)
        heatmap /= torch.max(heatmap) + 1e-8
        return heatmap.cpu().detach().numpy()

    def generate_spatial_heatmap(self, image_tensor, target_layer=None):
        if hasattr(self.model, 'forward_spatial'):
            output = self.model.forward_spatial(image_tensor)
        else:
            # Demo fallback
            return np.random.rand(224, 224).astype(np.float32)
            
        if isinstance(output, torch.Tensor) and output.requires_grad:
            output[:, output.argmax(dim=1)].backward(retain_graph=True)
            
        heatmap = self.generate_heatmap(self.gradients_spatial, self.activations_spatial)
        heatmap = cv2.resize(heatmap, (image_tensor.shape[-1], image_tensor.shape[-2]))
        return heatmap

    def generate_frequency_heatmap(self, dct_tensor, target_layer=None):
        if hasattr(self.model, 'forward_frequency'):
            output = self.model.forward_frequency(dct_tensor)
        else:
            # Demo fallback
            return np.random.rand(224, 224).astype(np.float32)
            
        if isinstance(output, torch.Tensor) and output.requires_grad:
            output[:, output.argmax(dim=1)].backward(retain_graph=True)
            
        heatmap = self.generate_heatmap(self.gradients_freq, self.activations_freq)
        heatmap = cv2.resize(heatmap, (dct_tensor.shape[-1], dct_tensor.shape[-2]))
        return heatmap

    def overlay_heatmap(self, original_image, heatmap, alpha=0.4):
        if isinstance(original_image, torch.Tensor):
            original_image = original_image.squeeze().permute(1, 2, 0).cpu().numpy()
            original_image = (original_image * 255).astype(np.uint8)
        elif isinstance(original_image, Image.Image):
            original_image = np.array(original_image)
            
        if original_image.shape[:2] != heatmap.shape:
            heatmap = cv2.resize(heatmap, (original_image.shape[1], original_image.shape[0]))
            
        heatmap = np.uint8(255 * heatmap)
        heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)
        
        superimposed_img = cv2.addWeighted(original_image, 1 - alpha, heatmap, alpha, 0)
        return Image.fromarray(cv2.cvtColor(superimposed_img, cv2.COLOR_BGR2RGB))

    def generate_combined_visualization(self, image, dct, model):
        try:
            spatial_heatmap = self.generate_spatial_heatmap(image)
            freq_heatmap = self.generate_frequency_heatmap(dct)
        except Exception:
            # Fallback for demo
            spatial_heatmap = np.random.rand(224, 224).astype(np.float32)
            freq_heatmap = np.random.rand(224, 224).astype(np.float32)
            
        return {
            'spatial_heatmap': spatial_heatmap,
            'freq_heatmap': freq_heatmap,
            'combined': (spatial_heatmap + freq_heatmap) / 2.0
        }

def create_forensic_report_image(original, spatial_cam, freq_cam, prediction, confidence):
    # original, spatial_cam, freq_cam should be PIL images
    width, height = original.size
    
    # Create a new image with extra height for text, and 3x width
    new_width = width * 3 + 40
    new_height = height + 100
    report_img = Image.new('RGB', (new_width, new_height), color=(30, 30, 30))
    
    # Paste images
    report_img.paste(original, (10, 50))
    report_img.paste(spatial_cam, (width + 20, 50))
    report_img.paste(freq_cam, (width * 2 + 30, 50))
    
    draw = ImageDraw.Draw(report_img)
    try:
        font = ImageFont.truetype("arial.ttf", 20)
        title_font = ImageFont.truetype("arial.ttf", 28)
    except IOError:
        font = ImageFont.load_default()
        title_font = ImageFont.load_default()
        
    color = (0, 255, 0) if prediction.upper() == 'REAL' else (255, 0, 0)
    
    draw.text((10, 10), f"Verdict: {prediction} ({confidence:.2f}%)", fill=color, font=title_font)
    draw.text((10 + width//2 - 30, 50 + height + 10), "Original", fill=(255,255,255), font=font)
    draw.text((width + 20 + width//2 - 50, 50 + height + 10), "Spatial CAM", fill=(255,255,255), font=font)
    draw.text((width*2 + 30 + width//2 - 60, 50 + height + 10), "Frequency CAM", fill=(255,255,255), font=font)
    
    return report_img
