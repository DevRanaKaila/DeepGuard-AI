import albumentations as A
from albumentations.pytorch import ToTensorV2

def get_train_transforms(img_size=256):
    """
    Returns albumentations transforms for training.
    """
    return A.Compose([
        A.Resize(height=img_size, width=img_size),
        A.HorizontalFlip(p=0.5),
        A.ImageCompression(quality_range=(40, 90), p=0.3),
        A.GaussianBlur(blur_limit=(3, 7), p=0.2),
        A.ColorJitter(brightness=0.15, contrast=0.15, p=0.3),
        A.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ToTensorV2()
    ])

def get_val_transforms(img_size=256):
    """
    Returns albumentations transforms for validation.
    """
    return A.Compose([
        A.Resize(height=img_size, width=img_size),
        A.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ToTensorV2()
    ])

def get_dct_augmentations():
    """
    Minimal augmentations for the DCT stream.
    """
    return A.Compose([
        A.HorizontalFlip(p=0.5),
        ToTensorV2()
    ])
