# DeepGuard AI: Dual-Stream Spatial and Frequency-Domain Deepfake Video Detection

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![PyTorch 2.0+](https://img.shields.io/badge/PyTorch-2.0+-ee4c2c.svg)](https://pytorch.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30+-ff4b4b.svg)](https://streamlit.io/)
[![AKTU B.Tech Mini Project](https://img.shields.io/badge/AKTU-CSE--AIML%20Sem%20VII-green.svg)](https://aktu.ac.in/)

**Student:** Dev Rana Kaila (Roll No: `2301531530023`)  
**Department:** Computer Science & Engineering (Artificial Intelligence & Machine Learning)  
**Institution:** Lloyd Institute of Engineering & Technology, Greater Noida  
**University:** Dr. A.P.J. Abdul Kalam Technical University (AKTU), Lucknow  
**Supervisor & Mini Project Coordinator:** Dr. Devendra Gautam (Associate Professor)  

---

## 📑 Project Deliverables

1. **`Dev_Rana_Kaila_Synopsis.pdf`** — **21-page official print-ready PDF** adhering to AKTU formatting rules (1.5" left margin, Times New Roman, cover page, certificate, declaration, abstract, 9 chapters, formal comparative tables, 10-week timeline, and IEEE references).
2. **`Dev_Rana_Kaila_Synopsis.docx`** — Fully styled editable Microsoft Word version.
3. **`Dev_Rana_Kaila_Synopsis.tex`** — Complete LaTeX source file for Overleaf compilation.
4. **`presentation/index.html`** — **10-slide interactive presentation** explaining the architecture visually for a general audience or evaluation committee.
5. **`app.py`** — Interactive **Streamlit forensic dashboard** with video/image upload, Plotly gauge meters, frame-by-frame analysis, and Grad-CAM visual heatmaps.
6. **`train.py`** & **`inference.py`** — Complete PyTorch training and inference pipelines.

---

## 🏛️ System Architecture

```
Input Video/Image
       │
       ▼
[MTCNN Face Detector] ──> Aligned Face Crop (256×256 RGB)
                               │
               ┌───────────────┴───────────────┐
               ▼                               ▼
     Stream I: Spatial Stream        Stream II: Frequency Stream
     EfficientNet-B4 Backbone        2D-DCT (Type-II Orthonormal)
     [B, 3, 256, 256]                [B, 1, 256, 256]
               │                               │
               ▼                               ▼
       Spatial Feature                 4-Stage Spectral CNN
       Vector (1,792-d)                Vector (512-d)
               │                               │
               └───────────────┬───────────────┘
                               ▼
                Attention-Gated Bilinear Fusion
                  g = σ(Wg [v_s || Wp v_f] + bg)
                   Fused Vector (1,024-d)
                               │
                               ▼
                     Classification Head
            FC(1024→256) ──> LayerNorm ──> ReLU
                   Dropout(0.4) ──> FC(256→1)
                               │
                               ▼
                    Sigmoid Classification
                0.0 (Authentic) <──> 1.0 (Deepfake)
```

---

## ⚡ Quick Start & Run Instructions

### 1. Install Dependencies
```bash
cd D:\mini-project
pip install -r requirements.txt
```

### 2. Launch the Streamlit Forensic Dashboard
```bash
streamlit run app.py
```
Open your browser at `http://localhost:8501`. You can upload any video or image (or use sample images in `demo/sample_faces/`) to test detection and view Grad-CAM heatmaps.

### 3. Open the Interactive Architecture Presentation
Simply double-click:
```
D:\mini-project\presentation\index.html
```
Use the `Left Arrow` / `Right Arrow` or on-screen buttons to navigate through the 10 slides.

### 4. Run Standalone Inference (CLI)
```bash
# Analyze a sample image
python inference.py --input demo/sample_faces/real_sample.jpg --output results/

# Analyze a video
python inference.py --input path/to/video.mp4 --output results/
```

### 5. Train the Model (with synthetic/demo dataset)
```bash
python train.py --epochs 10 --batch_size 16
```
*(If no external dataset path is passed, it automatically creates a demo dataset and executes full training with Cosine Annealing and early stopping).*

---

## 📊 Benchmark Targets

| Method | Domain | FF++ Raw Acc | FF++ c23 Acc | Cross-Dataset AUC |
| :--- | :--- | :---: | :---: | :---: |
| MesoNet-4 (Afchar et al.) | Spatial | 90.1% | 70.5% | 0.752 |
| XceptionNet (Rossler et al.) | Spatial | 98.5% | 89.3% | 0.924 |
| F3-Net (Qian et al.) | Frequency | 97.9% | 90.4% | 0.938 |
| **DeepGuard AI (Ours)** | **Dual-Stream** | **≥ 98.9%** | **≥ 94.2%** | **≥ 0.968** |

---

## 🎓 Viva & Project Defense Cheat-Sheet

- **Why Dual-Stream?**
  Spatial-only detectors (like standard CNNs looking at pixels) degrade drastically from 98% to 65% when videos are compressed on WhatsApp or social media. Frequency analysis (2D-DCT) exposes invariant artifacts caused by GAN upsampling layers that survive heavy compression.
- **Why 2D-DCT instead of FFT?**
  DCT uses real numbers only (energy compaction in top-left corner), avoiding complex arithmetic while providing high spectral correlation for image compression boundaries.
- **Why Attention-Gated Fusion?**
  Instead of simple concatenation, the gating mechanism dynamically shifts weight between spatial and spectral streams depending on how degraded or compressed the input frame is.
