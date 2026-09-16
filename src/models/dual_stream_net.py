"""
Dual-Stream Deepfake Detection Network.
Combines SpatialStream, FrequencyStream, and AttentionFusion for robust detection.
"""
import torch
import torch.nn as nn
from typing import Dict, Optional

# Relative imports from the same package
from .spatial_stream import SpatialStream
from .frequency_stream import FrequencyStream
from .fusion import AttentionFusion

class DualStreamNet(nn.Module):
    """
    Complete Dual-Stream model.
    Takes RGB images and their corresponding DCT spectra.
    """
    def __init__(self, pretrained: bool = True):
        """
        Initializes the DualStreamNet.

        Args:
            pretrained (bool): Whether to use pretrained weights for the spatial backbone.
        """
        super().__init__()
        
        self.spatial_stream = SpatialStream(pretrained=pretrained)
        self.frequency_stream = FrequencyStream()
        
        self.fusion = AttentionFusion(spatial_dim=1792, freq_dim=512, out_dim=1024)
        
        # Classification head
        self.classifier = nn.Sequential(
            nn.Linear(1024, 256),
            nn.LayerNorm(256),
            nn.ReLU(inplace=True),
            nn.Dropout(0.4),
            nn.Linear(256, 1)
        )

    def forward(self, x_rgb: torch.Tensor, x_dct: torch.Tensor) -> Dict[str, torch.Tensor]:
        """
        Forward pass.

        Args:
            x_rgb (torch.Tensor): RGB image tensor [B, 3, 256, 256].
            x_dct (torch.Tensor): DCT spectrum tensor [B, 1, 256, 256].

        Returns:
            Dict[str, torch.Tensor]: Dictionary containing logits, probabilities, and intermediate features.
        """
        # Spatial features [B, 1792]
        spatial_feats = self.spatial_stream(x_rgb)
        
        # Frequency features [B, 512]
        freq_feats = self.frequency_stream(x_dct)
        
        # Fused features [B, 1024]
        fused_feats = self.fusion(spatial_feats, freq_feats)
        
        # Logits [B, 1]
        logits = self.classifier(fused_feats)
        
        # Probabilities
        probs = torch.sigmoid(logits)
        
        return {
            'logits': logits,
            'probs': probs,
            'spatial_features': spatial_feats,
            'freq_features': freq_feats,
            'fused_features': fused_feats
        }

    @classmethod
    def load_pretrained(cls, checkpoint_path: str, device: Optional[torch.device] = None) -> 'DualStreamNet':
        """
        Loads a DualStreamNet model from a saved checkpoint.

        Args:
            checkpoint_path (str): Path to the saved weights.
            device (torch.device, optional): Device to load the model on.

        Returns:
            DualStreamNet: The loaded model.
        """
        if device is None:
            device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
            
        model = cls(pretrained=False)
        checkpoint = torch.load(checkpoint_path, map_location=device)
        
        # Checkpoint might contain state_dict directly or in 'model_state_dict'
        state_dict = checkpoint.get('model_state_dict', checkpoint)
        model.load_state_dict(state_dict)
        model.to(device)
        model.eval()
        
        return model

    def get_num_params(self) -> int:
        """
        Returns the total number of trainable parameters in the model.
        
        Returns:
            int: Number of trainable parameters.
        """
        return sum(p.numel() for p in self.parameters() if p.requires_grad)

    def freeze_spatial_backbone(self):
        """Freezes the spatial stream backbone."""
        self.spatial_stream.freeze_backbone()

    def unfreeze_spatial_backbone(self):
        """Unfreezes the spatial stream backbone."""
        self.spatial_stream.unfreeze_backbone()
