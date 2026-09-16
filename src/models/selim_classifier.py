"""
Selim Seferbekov's 1st-Place Kaggle DFDC Winning Classifier.
Architecture: tf_efficientnet_b7_ns / tf_efficientnet_b4_ns backbone + AdaptiveAvgPool + Linear.
Reference: https://github.com/selimsef/dfdc_deepfake_challenge
"""
import torch
import torch.nn as nn
from torch.nn.modules.dropout import Dropout
from torch.nn.modules.linear import Linear
from torch.nn.modules.pooling import AdaptiveAvgPool2d
import timm


class SelimDeepFakeClassifier(nn.Module):
    """
    Direct implementation of the 1st Place Kaggle DFDC DeepFakeClassifier.
    Uses NoisyStudent pre-trained EfficientNet backbones fine-tuned on the DFDC dataset.
    """
    def __init__(self, encoder: str = "tf_efficientnet_b7_ns", dropout_rate: float = 0.0):
        super().__init__()
        self.encoder = timm.create_model(encoder, pretrained=False)
        self.avg_pool = AdaptiveAvgPool2d((1, 1))
        self.dropout = Dropout(dropout_rate)
        
        # Determine feature dimension
        if hasattr(self.encoder, 'num_features'):
            features = self.encoder.num_features
        elif 'b7' in encoder:
            features = 2560
        elif 'b4' in encoder:
            features = 1792
        else:
            features = 2048
            
        self.fc = Linear(features, 1)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Forward pass returning raw logits.
        Args:
            x (torch.Tensor): Aligned face tensor [B, 3, H, W]
        Returns:
            torch.Tensor: Logits [B, 1]
        """
        x = self.encoder.forward_features(x)
        x = self.avg_pool(x).flatten(1)
        x = self.dropout(x)
        x = self.fc(x)
        return x

    @classmethod
    def load_from_checkpoint(cls, checkpoint_path: str, device: str = "cpu") -> "SelimDeepFakeClassifier":
        """
        Loads the pre-trained Kaggle 1st place weights.
        """
        model = cls(encoder="tf_efficientnet_b7_ns")
        ckpt = torch.load(checkpoint_path, map_location=device, weights_only=False)
        
        # Unwrap state dict if nested
        state_dict = ckpt.get('state_dict', ckpt.get('model', ckpt))
        
        # Remove module. prefix if trained with DataParallel
        clean_state_dict = {}
        for k, v in state_dict.items():
            clean_k = k.replace('module.', '')
            clean_state_dict[clean_k] = v
            
        model.load_state_dict(clean_state_dict, strict=False)
        model.to(device)
        model.eval()
        return model
