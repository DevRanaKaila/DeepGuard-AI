import os
import cv2
from tqdm import tqdm
from PIL import Image

class VideoProcessor:
    """
    Utility for processing videos for deepfake detection.
    """
    def __init__(self):
        pass

    def process_video(self, video_path, face_detector, output_dir=None, fps=5):
        """
        Extracts frames at a given FPS, detects faces, and optionally saves them.
        Returns a list of PIL Images (cropped faces).
        """
        cap = cv2.VideoCapture(video_path)
        video_fps = cap.get(cv2.CAP_PROP_FPS)
        if video_fps <= 0:
            video_fps = 30
            
        frame_interval = max(1, int(video_fps / fps))
        
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        
        faces = []
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
            
        current_frame = 0
        saved_count = 0
        
        with tqdm(total=frame_count, desc=f"Processing {os.path.basename(video_path)}") as pbar:
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                    
                if current_frame % frame_interval == 0:
                    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    pil_img = Image.fromarray(frame_rgb)
                    
                    face = face_detector.detect_and_crop(pil_img)
                    if face is not None:
                        faces.append(face)
                        if output_dir:
                            out_path = os.path.join(output_dir, f'face_{saved_count:04d}.jpg')
                            face.save(out_path)
                        saved_count += 1
                        
                current_frame += 1
                pbar.update(1)
                
        cap.release()
        return faces

    def get_video_info(self, video_path):
        cap = cv2.VideoCapture(video_path)
        fps = cap.get(cv2.CAP_PROP_FPS)
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        duration = frame_count / fps if fps > 0 else 0
        cap.release()
        
        return {
            'fps': fps,
            'duration': duration,
            'frame_count': frame_count,
            'resolution': (width, height)
        }

    def sample_frames(self, video_path, num_frames=30):
        cap = cv2.VideoCapture(video_path)
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        
        if frame_count <= 0:
            frame_count = num_frames
            
        step = max(1, frame_count // num_frames)
        frames = []
        
        for i in range(num_frames):
            cap.set(cv2.CAP_PROP_POS_FRAMES, min(i * step, frame_count - 1))
            ret, frame = cap.read()
            if not ret:
                break
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frames.append(Image.fromarray(frame_rgb))
            
        cap.release()
        return frames
