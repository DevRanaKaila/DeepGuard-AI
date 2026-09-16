import os
import glob
from pathlib import Path
import random

import cv2
import torch
from torch.utils.data import Dataset
from PIL import Image, ImageDraw
import numpy as np

class DeepfakeDataset(Dataset):
    """
    Dataset for loading deepfake detection images from a directory structure.
    """
    def __init__(self, root_dir: str, split: str = "train", transform=None, dct_transform=None, face_detector=None):
        self.root_dir = root_dir
        self.split = split
        self.transform = transform
        self.dct_transform = dct_transform
        self.face_detector = face_detector
        
        self.samples = []
        self._load_samples()

    def _load_samples(self):
        real_dir = os.path.join(self.root_dir, 'real')
        fake_dir = os.path.join(self.root_dir, 'fake')
        
        real_images = []
        if os.path.exists(real_dir):
            real_images = glob.glob(os.path.join(real_dir, '**', '*.[jp][pn]*[g]'), recursive=True)
            
        fake_images = []
        if os.path.exists(fake_dir):
            fake_images = glob.glob(os.path.join(fake_dir, '**', '*.[jp][pn]*[g]'), recursive=True)
            
        all_samples = [(p, 0) for p in real_images] + [(p, 1) for p in fake_images]
        all_samples = sorted(all_samples)
        random.seed(42)
        random.shuffle(all_samples)
        
        n_samples = len(all_samples)
        train_end = int(0.8 * n_samples)
        val_end = int(0.9 * n_samples)
        
        if self.split == 'train':
            self.samples = all_samples[:train_end]
        elif self.split == 'val':
            self.samples = all_samples[train_end:val_end]
        else:
            self.samples = all_samples[val_end:]
            
    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx: int):
        img_path, label = self.samples[idx]
        image = Image.open(img_path).convert('RGB')
        
        if self.face_detector:
            detected_face = self.face_detector.detect_and_crop(image)
            if detected_face is not None:
                image = detected_face
        
        image_np = np.array(image)
        
        transformed_image = image_np
        if self.transform:
            transformed = self.transform(image=image_np)
            transformed_image = transformed['image']
        elif isinstance(transformed_image, np.ndarray):
            transformed_image = torch.from_numpy(transformed_image).permute(2, 0, 1).float() / 255.0
            
        dct_feature = torch.zeros((1, 256, 256))
        if self.dct_transform:
            dct_feature = self.dct_transform(image_np)
            
        return {
            'image': transformed_image,
            'dct': dct_feature,
            'label': torch.tensor(label, dtype=torch.float32),
            'path': img_path
        }

class DeepfakeVideoDataset(Dataset):
    """
    Dataset for loading directly from video files.
    """
    def __init__(self, video_paths, labels, num_frames=10, transform=None, dct_transform=None, face_detector=None):
        self.video_paths = video_paths
        self.labels = labels
        self.num_frames = num_frames
        self.transform = transform
        self.dct_transform = dct_transform
        self.face_detector = face_detector

    def __len__(self):
        return len(self.video_paths)
        
    def __getitem__(self, idx: int):
        video_path = self.video_paths[idx]
        label = self.labels[idx]
        
        cap = cv2.VideoCapture(video_path)
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        if frame_count <= 0:
            frame_count = self.num_frames
            
        step = max(1, frame_count // self.num_frames)
        
        frames = []
        for i in range(self.num_frames):
            cap.set(cv2.CAP_PROP_POS_FRAMES, min(i * step, frame_count - 1))
            ret, frame = cap.read()
            if not ret:
                break
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            pil_img = Image.fromarray(frame_rgb)
            
            if self.face_detector:
                face = self.face_detector.detect_and_crop(pil_img)
                if face is not None:
                    pil_img = face
                    
            img_np = np.array(pil_img)
            frames.append(img_np)
            
        cap.release()
        
        if not frames:
            frames.append(np.zeros((256, 256, 3), dtype=np.uint8))
            
        selected_frame = random.choice(frames)
        
        transformed_img = selected_frame
        if self.transform:
            transformed = self.transform(image=selected_frame)
            transformed_img = transformed['image']
        else:
            transformed_img = torch.from_numpy(transformed_img).permute(2, 0, 1).float() / 255.0
            
        dct_feature = torch.zeros((1, 256, 256))
        if self.dct_transform:
            dct_feature = self.dct_transform(selected_frame)
            
        return {
            'image': transformed_img,
            'dct': dct_feature,
            'label': torch.tensor(label, dtype=torch.float32),
            'path': video_path
        }


def create_demo_dataset(output_dir: str, num_samples: int = 100):
    """
    Creates a synthetic dataset for testing the pipeline without a real dataset.
    Generates half 'real' and half 'fake' face-like images.
    """
    real_dir = os.path.join(output_dir, 'real', 'video_001')
    fake_dir = os.path.join(output_dir, 'fake', 'video_001')
    os.makedirs(real_dir, exist_ok=True)
    os.makedirs(fake_dir, exist_ok=True)
    
    num_real = num_samples // 2
    num_fake = num_samples - num_real
    
    # Generate real
    for i in range(num_real):
        img = Image.new('RGB', (256, 256), color=(200, 150, 100))
        draw = ImageDraw.Draw(img)
        draw.ellipse([64, 40, 192, 216], fill=(220, 180, 140))
        draw.ellipse([100, 100, 120, 115], fill=(50, 50, 50))
        draw.ellipse([136, 100, 156, 115], fill=(50, 50, 50))
        img.save(os.path.join(real_dir, f'frame_{i:03d}.jpg'))
        
    # Generate fake
    for i in range(num_fake):
        img = Image.new('RGB', (256, 256), color=(200, 150, 100))
        draw = ImageDraw.Draw(img)
        draw.ellipse([64, 40, 192, 216], fill=(220, 180, 140))
        draw.ellipse([100, 100, 120, 115], fill=(50, 50, 50))
        draw.ellipse([136, 100, 156, 115], fill=(50, 50, 50))
        
        img_np = np.array(img, dtype=np.float32)
        noise = np.random.normal(0, 15, img_np.shape)
        img_np = np.clip(img_np + noise, 0, 255).astype(np.uint8)
        
        for x in range(0, 256, 16):
            img_np[:, x] = (img_np[:, x] * 0.8).astype(np.uint8)
        for y in range(0, 256, 16):
            img_np[y, :] = (img_np[y, :] * 0.8).astype(np.uint8)
            
        fake_img = Image.fromarray(img_np)
        fake_img.save(os.path.join(fake_dir, f'frame_{i:03d}.jpg'))
