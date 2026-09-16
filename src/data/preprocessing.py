import os
import cv2
import numpy as np
from PIL import Image
try:
    from facenet_pytorch import MTCNN
except ImportError:
    MTCNN = None

class FaceDetector:
    """
    Face detection and preprocessing using MTCNN.
    """
    def __init__(self, device='cpu'):
        if MTCNN is None:
            print("Warning: facenet_pytorch not found. Face detector will use a fallback center crop.")
            self.mtcnn = None
        else:
            self.mtcnn = MTCNN(keep_all=True, device=device)

    def detect_and_crop(self, image, margin=0.15):
        """
        Detects the largest face and crops it with a margin.
        Returns a PIL Image of 256x256, or None if no face is detected.
        """
        if self.mtcnn is None:
            # Fallback center crop if MTCNN is missing
            width, height = image.size
            min_dim = min(width, height)
            left = (width - min_dim) / 2
            top = (height - min_dim) / 2
            right = (width + min_dim) / 2
            bottom = (height + min_dim) / 2
            return image.crop((left, top, right, bottom)).resize((256, 256))

        boxes, probs = self.mtcnn.detect(image)
        
        if boxes is None or len(boxes) == 0:
            return None
            
        # Find the largest face
        areas = (boxes[:, 2] - boxes[:, 0]) * (boxes[:, 3] - boxes[:, 1])
        largest_idx = np.argmax(areas)
        box = boxes[largest_idx]
        
        # Apply margin
        width = box[2] - box[0]
        height = box[3] - box[1]
        
        img_width, img_height = image.size
        
        x1 = max(0, int(box[0] - width * margin))
        y1 = max(0, int(box[1] - height * margin))
        x2 = min(img_width, int(box[2] + width * margin))
        y2 = min(img_height, int(box[3] + height * margin))
        
        face_img = image.crop((x1, y1, x2, y2))
        return face_img.resize((256, 256), Image.Resampling.LANCZOS)

def detect_and_crop_face(image, detector=None, margin=0.15):
    if detector is None:
        detector = FaceDetector()
    cropped = detector.detect_and_crop(image, margin=margin)
    if cropped is None:
        return image.resize((256, 256), Image.Resampling.LANCZOS)
    return cropped

def preprocess_face(face_image, size=256):
    """
    Normalizes a PIL image.
    """
    if face_image.size != (size, size):
        face_image = face_image.resize((size, size), Image.Resampling.LANCZOS)
    return face_image

def align_face(image, landmarks):
    """
    Dummy alignment function. Real implementation would rotate based on eye landmarks.
    """
    return image

def extract_frames_from_video(video_path, output_dir, fps=5):
    """
    Extracts frames from a video file at a specified FPS.
    """
    os.makedirs(output_dir, exist_ok=True)
    cap = cv2.VideoCapture(video_path)
    
    video_fps = cap.get(cv2.CAP_PROP_FPS)
    if video_fps <= 0:
        video_fps = 30
        
    frame_interval = max(1, int(video_fps / fps))
    
    frame_count = 0
    saved_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
            
        if frame_count % frame_interval == 0:
            out_path = os.path.join(output_dir, f'frame_{saved_count:04d}.jpg')
            cv2.imwrite(out_path, frame)
            saved_count += 1
            
        frame_count += 1
        
    cap.release()
    return saved_count
