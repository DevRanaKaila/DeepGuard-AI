"""
Frequency Stream Module for Dual-Stream Deepfake Detection.
Implements a 4-stage Spectral CNN with Depthwise Separable Convolutions to process DCT frequency maps.
"""
import torch
import torch.nn as nn

class DepthwiseSeparableConv(nn.Module):
    """
    Depthwise Separable Convolution block.
    Performs spatial convolution for each channel separately, followed by a 1x1 convolution across channels.
    """
    def __init__(self, in_channels: int, out_channels: int, kernel_size: int = 3, stride: int = 1, padding: int = 1):
        super().__init__()
        self.depthwise = nn.Conv2d(in_channels, in_channels, kernel_size=kernel_size, 
                                   stride=stride, padding=padding, groups=in_channels, bias=False)
        self.pointwise = nn.Conv2d(in_channels, out_channels, kernel_size=1, bias=False)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Args:
            x (torch.Tensor): Input tensor.
        Returns:
            torch.Tensor: Output tensor.
        """
        out = self.depthwise(x)
        out = self.pointwise(out)
        return out

class FrequencyStream(nn.Module):
    """
    Spectral CNN that processes DCT frequency maps.
    Input is expected to be [B, 1, 256, 256] and output is a 512-d feature vector.
    """
    def __init__(self):
        super().__init__()
        
        # Stage 1: Standard Conv
        self.stage1 = nn.Sequential(
            nn.Conv2d(1, 32, kernel_size=3, stride=1, padding=1, bias=False),
            nn.BatchNorm2d(32),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2, stride=2)  # Output: 128x128
        )
        
        # Stage 2: Depthwise Separable Conv
        self.stage2 = nn.Sequential(
            DepthwiseSeparableConv(32, 64, kernel_size=3, padding=1),
            nn.BatchNorm2d(64),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2, stride=2)  # Output: 64x64
        )
        
        # Stage 3: Depthwise Separable Conv
        self.stage3 = nn.Sequential(
            DepthwiseSeparableConv(64, 128, kernel_size=3, padding=1),
            nn.BatchNorm2d(128),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2, stride=2)  # Output: 32x32
        )
        
        # Stage 4: Depthwise Separable Conv
        self.stage4 = nn.Sequential(
            DepthwiseSeparableConv(128, 256, kernel_size=3, padding=1),
            nn.BatchNorm2d(256),
            nn.ReLU(inplace=True),
            nn.AdaptiveAvgPool2d((4, 4))  # Output: 4x4
        )
        
        # Final FC layer
        self.flatten = nn.Flatten()
        self.fc = nn.Linear(256 * 4 * 4, 512)
        
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Forward pass for the frequency stream.

        Args:
            x (torch.Tensor): DCT spectrum tensor of shape [B, 1, 256, 256].

        Returns:
            torch.Tensor: Extracted frequency features of shape [B, 512].
        """
        x = self.stage1(x)
        x = self.stage2(x)
        x = self.stage3(x)
        x = self.stage4(x)
        
        x = self.flatten(x)
        features = self.fc(x)
        return features
