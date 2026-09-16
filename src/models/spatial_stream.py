"""
Spatial Stream Module for Dual-Stream Deepfake Detection.
This module uses a pretrained EfficientNet-B4 to extract spatial features from RGB images.
"""
import torch
import torch.nn as nn
import timm

class SpatialStream(nn.Module):
    """
    EfficientNet-B4 spatial feature extractor.
    Removes the classification head and outputs a 1792-dimensional feature vector.
    """
    def __init__(self, pretrained: bool = True):
        """
        Initializes the SpatialStream model.

        Args:
            pretrained (bool): If True, loads pretrained weights.
        """
        super().__init__()
        # Load EfficientNet-B4 without the classifier head
        # efficientnet_b4 has 1792 output features before the classifier
        self.backbone = timm.create_model(
            'efficientnet_b4', 
            pretrained=pretrained, 
            num_classes=0,  # Remove classifier
            global_pool='avg'
        )
        self.feature_dim = 1792

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Forward pass for the spatial stream.

        Args:
            x (torch.Tensor): Input RGB tensor of shape [B, 3, 256, 256].

        Returns:
            torch.Tensor: Extracted spatial features of shape [B, 1792].
        """
        # x is [B, 3, 256, 256]
        features = self.backbone(x)
        # features is [B, 1792]
        return features

    def freeze_backbone(self):
        """Freezes the backbone parameters."""
        for param in self.backbone.parameters():
            param.requires_grad = False

    def unfreeze_backbone(self):
        """Unfreezes the backbone parameters."""
        for param in self.backbone.parameters():
            param.requires_grad = True
