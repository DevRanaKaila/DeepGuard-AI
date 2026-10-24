import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from build_report.helpers import (
    COLOR_PRIMARY, COLOR_DARK, add_heading_1, add_heading_2, add_heading_3,
    add_body_p, add_bullet_p, add_code_block, add_table_custom
)

def add_references_and_appendix(doc):
    # ==================== REFERENCES ====================
    add_heading_1(doc, "REFERENCES")

    references = [
        "[1] A. Rossler, D. Cozzolino, L. Verdoliva, C. Riess, J. Thies, and M. Niessner, “FaceForensics++: Learning to Detect "
        "Manipulated Facial Images,” in Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV), "
        "pp. 1–11, 2019.",
        
        "[2] J. Frank, T. Eisenhofer, L. Schonherr, A. Fischer, D. Kolossa, and T. Holz, “Leveraging Frequency Analysis for "
        "Deep Fake Image Recognition,” in Proceedings of the 37th International Conference on Machine Learning (ICML), "
        "PMLR, vol. 119, pp. 3247–3258, 2020.",
        
        "[3] M. Tan and Q. V. Le, “EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks,” in Proceedings "
        "of the 36th International Conference on Machine Learning (ICML), PMLR, vol. 97, pp. 6105–6114, 2019.",
        
        "[4] Y. Qian, G. Yin, L. Sheng, Z. Chen, and J. Shao, “Thinking in Frequency: Face Forgery Detection by Mining "
        "Frequency-Aware Clues,” in Proceedings of the European Conference on Computer Vision (ECCV), Springer, pp. 86–103, 2020.",
        
        "[5] Y. Li, X. Yang, P. Sun, H. Qi, and S. Lyu, “Celeb-DF: A Large-Scale Challenging Dataset for DeepFake Forensics,” "
        "in Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), pp. 3207–3216, 2020.",
        
        "[6] D. Afchar, V. Nozick, J. Yamagishi, and I. Echizen, “MesoNet: A Compact Facial Video Forgery Detection Network,” "
        "in IEEE International Workshop on Information Forensics and Security (WIFS), pp. 1–7, 2018.",
        
        "[7] R. Durall, M. Keuper, and J. Keuper, “Watch Your Up-Convolution: CNN Based Generative Deep Neural Networks Are "
        "Failing to Reproduce Spectral Distributions,” in Proceedings of the IEEE/CVF CVPR, pp. 7890–7899, 2020.",
        
        "[8] R. R. Selvaraju, M. Cogswell, A. Das, R. Vedaldi, D. Parikh, and D. Batra, “Grad-CAM: Visual Explanations from Deep "
        "Networks via Gradient-Based Localization,” International Journal of Computer Vision (IJCV), vol. 128, no. 2, pp. 336–359, 2020.",
        
        "[9] K. Zhang, Z. Zhang, Z. Li, and Y. Qiao, “Joint Face Detection and Alignment Using Multitask Cascaded Convolutional "
        "Networks,” IEEE Signal Processing Letters, vol. 23, no. 10, pp. 1499–1503, 2016.",
        
        "[10] I. Loshchilov and F. Hutter, “Decoupled Weight Decay Regularization,” in International Conference on Learning "
        "Representations (ICLR), pp. 1–10, 2019.",
        
        "[11] S. Seferbekov, “1st Place Solution to Kaggle Deepfake Detection Challenge,” Technical Report, Kaggle, 2020. "
        "[Online]. Available: https://github.com/selimsef/dfdc_deepfake_challenge.",
        
        "[12] I. Goodfellow, J. Pouget-Abadie, M. Mirza, B. Xu, D. Warde-Farley, S. Ozair, A. Courville, and Y. Bengio, “Generative "
        "Adversarial Nets,” Advances in Neural Information Processing Systems (NeurIPS), vol. 27, pp. 2672–2680, 2014.",
        
        "[13] K. He, X. Zhang, S. Ren, and J. Sun, “Deep Residual Learning for Image Recognition,” in Proceedings of the IEEE/CVF "
        "Conference on Computer Vision and Pattern Recognition (CVPR), pp. 770–778, 2016.",
        
        "[14] D. P. Kingma and M. Welling, “Auto-Encoding Variational Bayes,” in International Conference on Learning Representations "
        "(ICLR), pp. 1–14, 2014.",
        
        "[15] D. Rana Kaila, “DeepGuard AI: Dual-Stream Deepfake Detection Codebase,” [Online]. Available: "
        "https://github.com/DevRanaKaila/DeepGuard-AI. [Accessed: Oct. 23, 2026]."
    ]

    for ref in references:
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(3)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.line_spacing = 1.15
        p.paragraph_format.left_indent = Inches(0.4)
        p.paragraph_format.first_line_indent = Inches(-0.4)
        run = p.add_run(ref)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(9.5)

    doc.add_page_break()

    # ==================== APPENDIX ====================
    add_heading_1(doc, "APPENDIX")

    add_heading_2(doc, "Appendix A: Core Source Code Extracts")
    add_body_p(
        doc,
        "This appendix reproduces primary architectural source code components from the operational DeepGuard AI repository. "
        "The complete, version-controlled codebase is available at https://github.com/DevRanaKaila/DeepGuard-AI."
    )

    # A.1 DualStreamNet
    code_a1 = (
        "class DualStreamNet(nn.Module):\n"
        "    \"\"\"Unified Dual-Stream Network combining Spatial and Frequency streams.\"\"\"\n"
        "    def __init__(self, pretrained: bool = True):\n"
        "        super().__init__()\n"
        "        self.spatial_stream = SpatialStream(pretrained=pretrained)\n"
        "        self.frequency_stream = FrequencyStream()\n"
        "        self.fusion = AttentionFusion(spatial_dim=1792, freq_dim=512, out_dim=1024)\n"
        "        self.classifier = nn.Sequential(\n"
        "            nn.Linear(1024, 256),\n"
        "            nn.LayerNorm(256),\n"
        "            nn.ReLU(inplace=True),\n"
        "            nn.Dropout(0.4),\n"
        "            nn.Linear(256, 1)\n"
        "        )\n"
        "\n"
        "    def forward(self, x_rgb: torch.Tensor, x_dct: torch.Tensor) -> Dict[str, torch.Tensor]:\n"
        "        v_spatial = self.spatial_stream(x_rgb)\n"
        "        v_freq = self.frequency_stream(x_dct)\n"
        "        v_fused, gate = self.fusion(v_spatial, v_freq)\n"
        "        logits = self.classifier(v_fused)\n"
        "        probs = torch.sigmoid(logits)\n"
        "        return {\n"
        "            'logits': logits,\n"
        "            'probs': probs,\n"
        "            'gate_weight': gate,\n"
        "            'spatial_features': v_spatial,\n"
        "            'freq_features': v_freq,\n"
        "            'fused_features': v_fused\n"
        "        }\n"
    )
    add_code_block(doc, code_a1, title="A.1 DualStreamNet Architecture (src/models/dual_stream_net.py)")

    # A.2 FrequencyStream
    code_a2 = (
        "class FrequencyStream(nn.Module):\n"
        "    \"\"\"4-Stage Custom Spectral-CNN for 2D-DCT Feature Extraction.\"\"\"\n"
        "    def __init__(self, in_channels: int = 1, feature_dim: int = 512):\n"
        "        super().__init__()\n"
        "        self.features = nn.Sequential(\n"
        "            # Stage 1: Initial frequency receptive field\n"
        "            nn.Conv2d(in_channels, 32, kernel_size=3, stride=2, padding=1),\n"
        "            nn.BatchNorm2d(32),\n"
        "            nn.ReLU(inplace=True),\n"
        "            # Stage 2: Depthwise separable spectral filters\n"
        "            nn.Conv2d(32, 64, kernel_size=3, stride=2, padding=1),\n"
        "            nn.BatchNorm2d(64),\n"
        "            nn.ReLU(inplace=True),\n"
        "            # Stage 3: Mid-frequency feature maps\n"
        "            nn.Conv2d(64, 128, kernel_size=3, stride=2, padding=1),\n"
        "            nn.BatchNorm2d(128),\n"
        "            nn.ReLU(inplace=True),\n"
        "            # Stage 4: High-frequency artifact detection\n"
        "            nn.Conv2d(128, 256, kernel_size=3, stride=2, padding=1),\n"
        "            nn.BatchNorm2d(256),\n"
        "            nn.ReLU(inplace=True),\n"
        "            nn.AdaptiveAvgPool2d((1, 1))\n"
        "        )\n"
        "        self.fc = nn.Sequential(\n"
        "            nn.Linear(256, feature_dim),\n"
        "            nn.LayerNorm(feature_dim),\n"
        "            nn.ReLU(inplace=True)\n"
        "        )\n"
        "\n"
        "    def forward(self, x: torch.Tensor) -> torch.Tensor:\n"
        "        x = self.features(x)\n"
        "        x = torch.flatten(x, 1)\n"
        "        return self.fc(x)\n"
    )
    add_code_block(doc, code_a2, title="A.2 4-Stage Spectral-CNN (src/models/frequency_stream.py)")

    add_heading_2(doc, "Appendix B: Additional Material & Project Metadata")

    add_heading_3(doc, "B.1 Project Links and Version Control")
    add_bullet_p(doc, "Official GitHub Source Repository: https://github.com/DevRanaKaila/DeepGuard-AI")
    add_bullet_p(doc, "Local Interactive Forensic Dashboard: http://localhost:8501/")
    add_bullet_p(doc, "Kaggle Benchmark Challenge Baseline: https://github.com/selimsef/dfdc_deepfake_challenge")

    add_heading_3(doc, "B.2 Main Application Routes and CLI Commands")
    tb1_headers = ["Interface / Mode", "Command / Route", "Purpose and Target Subsystem"]
    tb1_rows = [
        ["Web Dashboard", "streamlit run app.py", "Launches interactive Streamlit forensic analysis web application"],
        ["Image Inference CLI", "python inference.py --input <path> --output results", "Executes single-image dual-stream inference with Grad-CAM"],
        ["Video Inference CLI", "python inference.py --input <video> --output results", "Processes continuous video stream at 5 FPS with temporal aggregation"],
        ["Model Training", "python train.py --config config.py", "Executes end-to-end model training with AdamW and label smoothing"],
        ["Figure Generator", "python generate_figures.py", "Generates high-resolution architecture diagrams and evaluation plots"]
    ]
    add_table_custom(
        doc, tb1_headers, tb1_rows,
        caption_text="Main application execution modes, CLI parameters, and operational commands",
        table_num="Table B.1",
        col_widths=[1.5, 2.3, 1.9]
    )

    add_heading_3(doc, "B.3 Repository Directory Structure")
    repo_structure = (
        "DeepGuard-AI/\n"
        "├── src/\n"
        "│   ├── data/                 # Video decoding, face alignment & 2D-DCT transforms\n"
        "│   │   ├── augmentation.py   # JPEG, blur, and color jitter augmentations\n"
        "│   │   ├── dataset.py        # FaceForensics++ & Celeb-DF v2 data loaders\n"
        "│   │   ├── dct_transform.py  # 2D-DCT-II & Radial Azimuthal Spectrum A(r)\n"
        "│   │   └── preprocessing.py  # MTCNN face landmark tracking & crop extraction\n"
        "│   ├── models/               # Neural network architectures\n"
        "│   │   ├── dual_stream_net.py # Complete unified DualStreamNet model\n"
        "│   │   ├── frequency_stream.py# 4-stage custom Spectral-CNN\n"
        "│   │   ├── fusion.py         # Attention-Gated Bilinear Fusion module\n"
        "│   │   ├── selim_classifier.py# Kaggle DFDC 1st-place champion backbone\n"
        "│   │   └── spatial_stream.py # Pretrained EfficientNet-B4 spatial backbone\n"
        "│   └── utils/                # Evaluation & visualization utilities\n"
        "│       ├── gradcam.py        # Dual-stream Grad-CAM heatmap generator\n"
        "│       ├── metrics.py        # AUC-ROC, EER, and confusion matrix evaluators\n"
        "│       └── video_processor.py# Uniform temporal frame extraction engine\n"
        "├── checkpoints/              # Model weights (.pth) & training checkpoints\n"
        "├── demo/                     # Sample authentic & deepfake test videos / faces\n"
        "├── results/                  # Generated forensic reports, heatmaps & JSON logs\n"
        "├── report_assets/            # High-resolution architectural diagrams & plots\n"
        "├── app.py                    # Interactive Streamlit forensic web application\n"
        "├── inference.py              # Standalone CLI and API inference engine\n"
        "├── train.py                  # PyTorch training pipeline with AMP & Cosine Annealing\n"
        "├── config.py                 # Global hyperparameters and directory configurations\n"
        "└── requirements.txt          # Production Python package dependencies\n"
    )
    add_code_block(doc, repo_structure, title="Repository Directory Structure (github.com/DevRanaKaila/DeepGuard-AI)")
