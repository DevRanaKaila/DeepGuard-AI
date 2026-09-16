"""
Attention-Gated Bilinear Fusion Module.
Fuses spatial and frequency features using an attention mechanism.
"""
import torch
import torch.nn as nn

class AttentionFusion(nn.Module):
    """
    Fuses spatial features (1792-d) and frequency features (512-d).
    Uses a learnable projection and a sigmoid attention gate.
    """
    def __init__(self, spatial_dim: int = 1792, freq_dim: int = 512, out_dim: int = 1024):
        """
        Initializes the AttentionFusion module.

        Args:
            spatial_dim (int): Dimension of spatial features. Default 1792.
            freq_dim (int): Dimension of frequency features. Default 512.
            out_dim (int): Dimension of the output fused vector. Default 1024.
        """
        super().__init__()
        
        self.spatial_dim = spatial_dim
        
        # Projection layer to match spatial dimension
        self.freq_proj = nn.Linear(freq_dim, spatial_dim)
        
        # Attention gate weights
        # Computes gate based on concatenated spatial and projected frequency features
        self.gate = nn.Sequential(
            nn.Linear(spatial_dim * 2, spatial_dim),
            nn.Sigmoid()
        )
        
        # Final projection down to out_dim
        self.final_proj = nn.Linear(spatial_dim * 2, out_dim)

    def forward(self, spatial_feats: torch.Tensor, freq_feats: torch.Tensor) -> torch.Tensor:
        """
        Forward pass for fusion.

        Args:
            spatial_feats (torch.Tensor): Spatial features [B, 1792].
            freq_feats (torch.Tensor): Frequency features [B, 512].

        Returns:
            torch.Tensor: Fused feature vector [B, 1024].
        """
        # Project frequency features to 1792
        freq_proj = self.freq_proj(freq_feats) # [B, 1792]
        
        # Concatenate for gating mechanism
        concat_feats = torch.cat((spatial_feats, freq_proj), dim=1) # [B, 3584]
        
        # Compute attention gate
        g = self.gate(concat_feats) # [B, 1792]
        
        # Apply gate
        spatial_gated = g * spatial_feats
        freq_gated = (1 - g) * freq_proj
        
        # Concatenate gated features
        v_fused = torch.cat((spatial_gated, freq_gated), dim=1) # [B, 3584]
        
        # Final projection
        out = self.final_proj(v_fused) # [B, 1024]
        return out
