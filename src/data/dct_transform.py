"""
2D Discrete Cosine Transform (DCT) Module.
Computes 2D-DCT spectrum and radial power spectrum for frequency-domain analysis.
"""
import torch
import numpy as np
from PIL import Image
import scipy.fft
import matplotlib.pyplot as plt
from typing import Union, Tuple

class DCTTransform:
    """
    PyTorch-compatible transform that takes an image and returns its DCT spectrum.
    """
    def __init__(self, log_scale: bool = True):
        self.log_scale = log_scale

    def __call__(self, img: Union[Image.Image, np.ndarray, torch.Tensor]) -> torch.Tensor:
        """
        Applies 2D-DCT to the input image.

        Args:
            img: Input image (PIL Image, numpy array, or torch Tensor).

        Returns:
            torch.Tensor: DCT spectrum of shape [1, H, W].
        """
        # Convert to numpy grayscale
        if isinstance(img, Image.Image):
            img_np = np.array(img.convert('L'), dtype=np.float32)
        elif isinstance(img, torch.Tensor):
            if img.ndim == 3 and img.shape[0] == 3:
                # RGB to Grayscale using standard weights
                img = 0.2989 * img[0] + 0.5870 * img[1] + 0.1140 * img[2]
            elif img.ndim == 3 and img.shape[0] == 1:
                img = img.squeeze(0)
            img_np = img.cpu().numpy().astype(np.float32)
        else:
            img_np = np.asarray(img, dtype=np.float32)
            if img_np.ndim == 3:
                if img_np.shape[2] == 3:
                    # RGB to Grayscale
                    img_np = np.dot(img_np[..., :3], [0.2989, 0.5870, 0.1140])

        # Compute 2D DCT (Type-II, orthonormalized)
        dct_coeffs = scipy.fft.dctn(img_np, type=2, norm='ortho')
        magnitude = np.abs(dct_coeffs)

        if self.log_scale:
            magnitude = np.log1p(magnitude)

        # Convert back to tensor [1, H, W]
        return torch.from_numpy(magnitude).unsqueeze(0).float()


def compute_radial_spectrum(dct_coeffs: np.ndarray) -> np.ndarray:
    """
    Computes the Azimuthal (Radial) Average Power Spectrum A(r).

    Args:
        dct_coeffs (np.ndarray): 2D array of DCT coefficients.

    Returns:
        np.ndarray: 1D radial average power spectrum.
    """
    h, w = dct_coeffs.shape
    y, x = np.indices((h, w))
    center_y, center_x = 0, 0 # DCT low frequencies are at the top-left origin
    
    r = np.sqrt((x - center_x)**2 + (y - center_y)**2)
    r = r.astype(np.int32)

    tbin = np.bincount(r.ravel(), (dct_coeffs**2).ravel())
    nr = np.bincount(r.ravel())
    radial_profile = tbin / np.maximum(nr, 1) # avoid division by zero
    
    return radial_profile


def plot_dct_spectrum(image: Union[Image.Image, np.ndarray], save_path: str = None) -> None:
    """
    Computes and plots the DCT spectrum of an image.

    Args:
        image: Input image.
        save_path: Optional path to save the plot.
    """
    transform = DCTTransform(log_scale=True)
    dct_tensor = transform(image)
    dct_np = dct_tensor.squeeze(0).numpy()

    plt.figure(figsize=(8, 6))
    plt.imshow(dct_np, cmap='viridis')
    plt.colorbar(label='Log Magnitude')
    plt.title('2D DCT Spectrum')
    
    if save_path:
        plt.savefig(save_path, bbox_inches='tight')
        plt.close()
    else:
        plt.show()
