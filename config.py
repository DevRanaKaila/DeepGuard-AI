"""
Configuration settings for the Dual-Stream Deepfake Detection project.
"""
from dataclasses import dataclass
import torch
import os

@dataclass
class Config:
    """Project configuration parameters."""
    # Data parameters
    IMG_SIZE: int = 256
    BATCH_SIZE: int = 16
    
    # Training hyperparameters
    LR: float = 1e-4
    WEIGHT_DECAY: float = 1e-4
    EPOCHS: int = 40
    PATIENCE: int = 6
    LABEL_SMOOTHING: float = 0.1
    DROPOUT: float = 0.4
    
    # Architecture dimensions
    SPATIAL_DIM: int = 1792
    FREQ_DIM: int = 512
    FUSED_DIM: int = 1024
    
    # Paths
    BASE_DIR: str = os.path.dirname(os.path.abspath(__file__))
    DATA_DIR: str = os.path.join(BASE_DIR, 'data')
    CHECKPOINT_DIR: str = os.path.join(BASE_DIR, 'checkpoints')
    
    # Device auto-detection
    DEVICE: str = 'cuda' if torch.cuda.is_available() else ('mps' if torch.backends.mps.is_available() else 'cpu')

    def __post_init__(self):
        """Ensure directories exist."""
        os.makedirs(self.DATA_DIR, exist_ok=True)
        os.makedirs(self.CHECKPOINT_DIR, exist_ok=True)

# Global configuration instance
config = Config()
