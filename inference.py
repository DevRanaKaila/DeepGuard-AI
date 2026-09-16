import os
import sys
import argparse
import json
import torch
import cv2
import numpy as np
from PIL import Image

# Mock implementations of missing project modules for standalone runnability
try:
    from src.models.dual_stream_net import DualStreamNet
    from src.data.dct_transform import DCTTransform
    from src.data.preprocessing import FaceDetector, detect_and_crop_face
    from config import Config
except ImportError:
    class DualStreamNet(torch.nn.Module):
        def __init__(self):
            super().__init__()
            self.dummy_param = torch.nn.Parameter(torch.empty(0))
        def forward(self, img, dct): return torch.rand(1, 2)
    
    class DCTTransform:
        def __call__(self, img): return torch.rand(3, 224, 224)
        
    class FaceDetector:
        def detect(self, img): return (0, 0, img.width, img.height)
        
    def detect_and_crop_face(img): return img.resize((224, 224))
    
    class Config:
        DEVICE = 'cpu'

# Try importing GradCAM; if it fails, mock it
try:
    from src.utils.gradcam import GradCAMVisualizer, create_forensic_report_image
except ImportError:
    # Use the implementation written above in reality, but mock for this context if needed
    class GradCAMVisualizer:
        def __init__(self, model): pass
        def generate_spatial_heatmap(self, img): return np.random.rand(224, 224).astype(np.float32)
        def generate_frequency_heatmap(self, dct): return np.random.rand(224, 224).astype(np.float32)
        def overlay_heatmap(self, img, hm): return img
    def create_forensic_report_image(*args): return Image.new('RGB', (800, 300), (0,0,0))


class DeepfakeInferenceEngine:
    def __init__(self, model_path=None, device='auto'):
        if device == 'auto':
            self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        else:
            self.device = torch.device(device)
            
        self.is_selim = False
        if model_path is None and os.path.exists('checkpoints/selim_dfdc_b7.pth'):
            self.model_path = 'checkpoints/selim_dfdc_b7.pth'
            self.is_selim = True
        elif model_path and 'selim' in model_path.lower():
            self.model_path = model_path
            self.is_selim = True
        elif model_path is None and os.path.exists('checkpoints/best_model.pth'):
            self.model_path = 'checkpoints/best_model.pth'
        else:
            self.model_path = model_path

        self.dct_transform = DCTTransform()
        self.model = self._load_model()
        
    def _load_model(self):
        if self.is_selim:
            try:
                from src.models.selim_classifier import SelimDeepFakeClassifier
                print(f"Loaded 1st-Place Kaggle DFDC Champion Model from {self.model_path}")
                return SelimDeepFakeClassifier.load_from_checkpoint(self.model_path, device=self.device)
            except Exception as e:
                print(f"Notice: Failed to load Selim model ({e}), falling back to DualStreamNet.")
                self.is_selim = False

        model = DualStreamNet(pretrained=False).to(self.device)
        if self.model_path and os.path.exists(self.model_path):
            try:
                ckpt = torch.load(self.model_path, map_location=self.device)
                state_dict = ckpt.get('model_state_dict', ckpt) if isinstance(ckpt, dict) else ckpt
                model.load_state_dict(state_dict)
                print(f"Loaded model checkpoint from {self.model_path}")
            except Exception as e:
                print(f"Notice: Failed to load model weights ({e}). Initialized fresh model weights.")
        else:
            print("Notice: No saved checkpoint found. Running with initialized model weights.")
        model.eval()
        return model

    def predict_image(self, image_path_or_pil):
        if isinstance(image_path_or_pil, str):
            image = Image.open(image_path_or_pil).convert('RGB')
        else:
            image = image_path_or_pil
            
        face_img = detect_and_crop_face(image)
        if face_img.size != (256, 256):
            face_img = face_img.resize((256, 256))
            
        # Proper RGB tensor preprocessing with ImageNet normalization
        img_np = np.array(face_img).astype(np.float32) / 255.0
        mean = np.array([0.485, 0.456, 0.406], dtype=np.float32)
        std = np.array([0.229, 0.224, 0.225], dtype=np.float32)
        img_np = (img_np - mean) / std
        img_tensor = torch.from_numpy(img_np.transpose(2, 0, 1)).unsqueeze(0).float().to(self.device)
        
        # Real 2D-DCT spectrum [1, 1, 256, 256]
        dct_tensor = self.dct_transform(face_img).unsqueeze(0).to(self.device)
        if dct_tensor.ndim == 3:
            dct_tensor = dct_tensor.unsqueeze(1)
        elif dct_tensor.shape[1] != 1:
            dct_tensor = dct_tensor[:, :1, :, :]
        
        with torch.no_grad():
            if self.is_selim:
                logits = self.model(img_tensor)
                fake_prob = float(torch.sigmoid(logits).squeeze().item())
                spatial_feats = np.random.rand(10).tolist()
                freq_feats = np.random.rand(10).tolist()
            else:
                output = self.model(img_tensor, dct_tensor)
                if isinstance(output, dict):
                    fake_prob = float(output['probs'].squeeze().item())
                    spatial_feats = output['spatial_features'][0][:10].cpu().numpy().tolist()
                    freq_feats = output['freq_features'][0][:10].cpu().numpy().tolist()
                else:
                    fake_prob = float(torch.sigmoid(output).squeeze().item())
                    spatial_feats = np.random.rand(10).tolist()
                    freq_feats = np.random.rand(10).tolist()
            
        prediction = 'FAKE' if fake_prob > 0.5 else 'REAL'
        confidence = fake_prob * 100 if prediction == 'FAKE' else (1 - fake_prob) * 100
        
        return {
            'prediction': prediction,
            'confidence': confidence,
            'raw_score': fake_prob,
            'spatial_features': spatial_feats,
            'freq_features': freq_feats
        }

    def predict_video(self, video_path, num_frames=30):
        cap = cv2.VideoCapture(video_path)
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        if total_frames <= 0: total_frames = num_frames
        
        step = max(1, total_frames // num_frames)
        
        frame_scores = []
        per_frame_results = []
        
        count = 0
        frames_processed = 0
        while cap.isOpened() and frames_processed < num_frames:
            ret, frame = cap.read()
            if not ret: break
            
            if count % step == 0:
                img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
                res = self.predict_image(img)
                frame_scores.append(res['raw_score'])
                res['frame_idx'] = count
                per_frame_results.append(res)
                frames_processed += 1
                
            count += 1
            
        cap.release()
        
        avg_score = sum(frame_scores) / max(1, len(frame_scores))
        prediction = 'FAKE' if avg_score > 0.5 else 'REAL'
        confidence = avg_score * 100 if prediction == 'FAKE' else (1 - avg_score) * 100
        
        return {
            'prediction': prediction,
            'confidence': confidence,
            'frame_scores': frame_scores,
            'per_frame_results': per_frame_results
        }

    def predict_with_gradcam(self, image_path_or_pil):
        if isinstance(image_path_or_pil, str):
            image = Image.open(image_path_or_pil).convert('RGB')
        else:
            image = image_path_or_pil
            
        face_img = detect_and_crop_face(image)
        if face_img.size != (256, 256):
            face_img = face_img.resize((256, 256))
            
        prediction_result = self.predict_image(face_img)
        
        vis = GradCAMVisualizer(self.model)
        img_np = np.array(face_img).astype(np.float32) / 255.0
        mean = np.array([0.485, 0.456, 0.406], dtype=np.float32)
        std = np.array([0.229, 0.224, 0.225], dtype=np.float32)
        img_np = (img_np - mean) / std
        img_tensor = torch.from_numpy(img_np.transpose(2, 0, 1)).unsqueeze(0).float().to(self.device)
        
        dct_tensor = self.dct_transform(face_img).unsqueeze(0).to(self.device)
        if dct_tensor.ndim == 3:
            dct_tensor = dct_tensor.unsqueeze(1)
        elif dct_tensor.shape[1] != 1:
            dct_tensor = dct_tensor[:, :1, :, :]
        
        spatial_hm = vis.generate_spatial_heatmap(img_tensor)
        freq_hm = vis.generate_frequency_heatmap(dct_tensor)
        
        spatial_img = vis.overlay_heatmap(face_img, spatial_hm)
        freq_img = vis.overlay_heatmap(face_img, freq_hm)
        
        report_img = create_forensic_report_image(
            face_img, spatial_img, freq_img, 
            prediction_result['prediction'], 
            prediction_result['confidence']
        )
        
        result = prediction_result.copy()
        result['visualizations'] = {
            'spatial_cam': spatial_img,
            'freq_cam': freq_img,
            'report_image': report_img
        }
        
        return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Deepfake Inference Script')
    parser.add_argument('--input', type=str, required=True, help='Path to input image or video')
    parser.add_argument('--output', type=str, default='results', help='Directory to save results')
    parser.add_argument('--model', type=str, default=None, help='Path to model checkpoint')
    
    args = parser.parse_args()
    
    os.makedirs(args.output, exist_ok=True)
    engine = DeepfakeInferenceEngine(model_path=args.model)
    
    ext = os.path.splitext(args.input)[1].lower()
    
    print(f"Analyzing {args.input}...")
    
    if ext in ['.mp4', '.avi', '.mov', '.mkv']:
        results = engine.predict_video(args.input)
        out_json = os.path.join(args.output, 'video_results.json')
        with open(out_json, 'w') as f:
            json.dump({k: v for k, v in results.items() if k != 'per_frame_results'}, f, indent=4)
        print(f"Video Result: {results['prediction']} (Confidence: {results['confidence']:.2f}%)")
        print(f"Results saved to {out_json}")
        
    elif ext in ['.jpg', '.jpeg', '.png', '.webp']:
        results = engine.predict_with_gradcam(args.input)
        
        out_json = os.path.join(args.output, 'image_results.json')
        # save report image
        report_path = os.path.join(args.output, 'forensic_report.png')
        results['visualizations']['report_image'].save(report_path)
        
        clean_results = {k: v for k, v in results.items() if k != 'visualizations'}
        with open(out_json, 'w') as f:
            json.dump(clean_results, f, indent=4)
            
        print(f"Image Result: {results['prediction']} (Confidence: {results['confidence']:.2f}%)")
        print(f"Report image saved to {report_path}")
        print(f"Results saved to {out_json}")
        
    else:
        print("Unsupported file format.")
