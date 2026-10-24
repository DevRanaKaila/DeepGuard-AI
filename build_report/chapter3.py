from build_report.helpers import (
    add_heading_1, add_heading_2, add_heading_3, add_body_p, add_bullet_p,
    add_figure, add_table_custom
)

def add_chapter_3(doc):
    add_heading_1(doc, "CHAPTER 3: SYSTEM ANALYSIS AND DESIGN")

    add_body_p(
        doc,
        "This chapter presents a comprehensive engineering analysis and architectural specification of DeepGuard AI. "
        "It establishes the formal functional and non-functional requirements, evaluates multi-dimensional feasibility, "
        "delineates the layered system topology, details the data flow and architectural models, and establishes data governance "
        "and security protocols for forensic chain-of-custody."
    )

    add_heading_2(doc, "3.1 Requirement Analysis")

    add_heading_3(doc, "3.1.1 Functional Requirements")
    add_body_p(
        doc,
        "The functional capabilities of DeepGuard AI are categorized into thirteen explicit requirements (FR1 to FR13), "
        "all of which are fully implemented, verified, and operational in the system."
    )

    t31_headers = ["ID", "Requirement Specification", "Target Subsystem", "Forensic Role"]
    t31_rows = [
        ["FR1", "Demux input video streams (MP4/AVI/MOV) and extract frames at uniform 5 FPS temporal intervals.", "Video Ingestion", "System Pipeline"],
        ["FR2", "Execute MTCNN cascade to detect facial landmarks, align pose, and extract 256x256 crops with 15% margin.", "Preprocessing", "Automated Preprocessor"],
        ["FR3", "Normalize RGB face tensors using ImageNet mean [0.485, 0.456, 0.406] and std [0.229, 0.224, 0.225].", "Spatial Stream", "Spatial Backbone"],
        ["FR4", "Compute 2D Discrete Cosine Transform (DCT-II) with orthonormal scaling on grayscale facial crops.", "Frequency Stream", "Spectral Engine"],
        ["FR5", "Calculate logarithmic spectral energy S(u,v) = log(1 + |F(u,v)|) to expose high-frequency anomalies.", "Frequency Stream", "Spectral Engine"],
        ["FR6", "Extract 1792-dimensional structural visual embedding via EfficientNet-B4 compound scaled backbone.", "Spatial Stream", "Feature Extractor"],
        ["FR7", "Extract 512-dimensional spectral representation via 4-stage depthwise separable Spectral-CNN.", "Frequency Stream", "Feature Extractor"],
        ["FR8", "Fuse spatial and frequency embeddings dynamically using Attention-Gated Bilinear Combination.", "Fusion Module", "Attention Gate"],
        ["FR9", "Compute calibrated real-versus-fake classification probability and confidence percentage score.", "Classification Head", "Inference Engine"],
        ["FR10", "Generate spatial-domain Grad-CAM heatmaps identifying boundary and texture manipulation clues.", "Explainability (XAI)", "Forensic Examiner"],
        ["FR11", "Generate frequency-domain Grad-CAM heatmaps highlighting periodic GAN upsampling spectral spikes.", "Explainability (XAI)", "Forensic Examiner"],
        ["FR12", "Compute video-level temporal authenticity aggregation with frame-by-frame probability trajectories.", "Temporal Engine", "Video Forensics"],
        ["FR13", "Generate and export verifiable PDF Forensic Verification Reports containing SHA-256 hashes.", "Reporting Engine", "Forensic Compliance"]
    ]
    add_table_custom(
        doc, t31_headers, t31_rows,
        caption_text="Functional requirements of DeepGuard AI forensic platform",
        table_num="Table 3.1",
        col_widths=[0.6, 2.7, 1.2, 1.2]
    )

    add_heading_3(doc, "3.1.2 Non-Functional Requirements")
    add_body_p(
        doc,
        "The non-functional requirements govern the performance, robustness, security, and usability benchmarks of the system."
    )

    t32_headers = ["Quality Attribute", "Requirement Specification and Benchmark Target", "Verification Method"]
    t32_rows = [
        ["Inference Latency", "Per-frame processing speed must not exceed 50 milliseconds on GPU (<120ms on CPU).", "Automated Benchmark Timer"],
        ["Compression Resilience", "Detection accuracy on c40 heavy compression must remain ≥88.0% (AUC-ROC ≥0.900).", "FaceForensics++ c40 Evaluation"],
        ["Forensic Explainability", "Every prediction must be accompanied by localized spatial and spectral heatmaps.", "Grad-CAM Activation Inspection"],
        ["Memory Footprint", "Total model parameters must remain under 25 million weights (<150 MB checkpoint).", "PyTorch Parameter Counter"],
        ["Data Integrity", "Video uploads must be processed in non-destructive read-only memory buffers.", "SHA-256 Checksum Validation"],
        ["Usability", "Interface must provide intuitive drag-and-drop video upload and real-time Plotly telemetry.", "Examiner Usability Walkthrough"],
        ["Cross-Dataset Robustness", "Model trained on FF++ must achieve AUC-ROC ≥0.950 on unseen Celeb-DF v2.", "Cross-Dataset Generalization Test"]
    ]
    add_table_custom(
        doc, t32_headers, t32_rows,
        caption_text="Non-functional requirements and target quality benchmarks",
        table_num="Table 3.2",
        col_widths=[1.4, 2.8, 1.5]
    )

    add_heading_3(doc, "3.1.3 Hardware and Software Requirements")
    add_body_p(
        doc,
        "The computational specifications for local development, model training, and production inference are detailed in Table 3.3."
    )

    t33_headers = ["Subsystem / Component", "Minimum Specification", "Recommended Production Specification"]
    t33_rows = [
        ["Host Operating System", "Windows 10 64-bit / Ubuntu 20.04 LTS", "Windows 11 64-bit / Ubuntu 22.04 LTS"],
        ["Processor (CPU)", "Intel Core i5 (8th Gen+) or AMD Ryzen 5", "Intel Core i7/i9 (12th Gen+) or AMD Ryzen 7/9"],
        ["System Memory (RAM)", "8 GB DDR4", "16 GB – 32 GB DDR4/DDR5"],
        ["Graphics Processing (GPU)", "NVIDIA GTX 1650 (4 GB VRAM) / CPU Fallback", "NVIDIA RTX 3060 / 4070 (8 GB – 12 GB VRAM, CUDA 11.8+)"],
        ["Secondary Storage", "20 GB free solid-state drive (SSD)", "100 GB NVMe PCIe SSD (for FF++ benchmarks)"],
        ["Programming Runtime", "Python 3.10", "Python 3.11 / 3.12 (64-bit)"],
        ["Core Frameworks", "PyTorch 2.0+, torchvision 0.15+, timm", "PyTorch 2.2+ with CUDA acceleration & AMP"],
        ["Vision & Signal Processing", "OpenCV 4.8+, SciPy 1.11+, Pillow 10.0+", "OpenCV (FFmpeg-enabled), SciPy, Albumentations"],
        ["Telemetry Dashboard", "Streamlit 1.28+, Plotly 5.17+", "Streamlit 1.35+, Plotly Express, ReportLab / Word COM"]
    ]
    add_table_custom(
        doc, t33_headers, t33_rows,
        caption_text="Hardware and software engineering specifications",
        table_num="Table 3.3",
        col_widths=[1.5, 2.1, 2.1]
    )

    add_heading_2(doc, "3.2 Feasibility Study")
    add_body_p(
        doc,
        "A rigorous multi-criteria feasibility study was conducted to validate the viability of DeepGuard AI:"
    )
    add_bullet_p(
        doc,
        "Technical Feasibility: The core technologies—PyTorch, torchvision, timm, SciPy, and OpenCV—are mature, robustly maintained, "
        "and extensively documented. By leveraging pre-trained EfficientNet backbones on ImageNet and closed-form 2D-DCT mathematics, "
        "the architecture avoids unstable custom CUDA kernels. Automated Mixed Precision (AMP) enables fast training within academic "
        "hardware limits. The full pipeline was successfully built, trained, and validated locally, confirming technical feasibility."
    )
    add_bullet_p(
        doc,
        "Economic Feasibility: All underlying software libraries, machine learning frameworks, dataset loaders, and dashboard tools are "
        "fully open-source under permissive licenses (Apache 2.0, MIT, BSD). Development and evaluation were accomplished using standard "
        "academic computing workstations without requiring enterprise cloud compute credits. Operating costs for deploying the Streamlit "
        "forensic dashboard are near-zero, proving exceptional economic feasibility."
    )
    add_bullet_p(
        doc,
        "Operational Feasibility: The web dashboard eliminates command-line friction by offering intuitive video drag-and-drop, automated "
        "face extraction, transparent color-coded gauges, and one-click PDF forensic certificates. Non-technical investigators and fintech "
        "compliance analysts require zero prior machine learning knowledge to execute high-assurance verification, ensuring seamless operational adoption."
    )

    add_heading_2(doc, "3.3 System Architecture")
    add_body_p(
        doc,
        "DeepGuard AI follows a layered, modular architectural pattern that decouples presentation, orchestration, model inference, "
        "signal transformation, and persistence. Figure 3.1 illustrates the layered system topology."
    )

    add_figure(
        doc,
        r'D:\mini-project\SUBMISSION\1_system_architecture_overview.png',
        caption_text="Layered architecture of the DeepGuard AI forensic platform showing data ingestion, dual-stream feature extraction, attention gating, and XAI telemetry",
        fig_num="Figure 3.1",
        width_in=5.4
    )

    add_body_p(
        doc,
        "The architecture consists of five coordinated tiers: (1) Ingestion Layer (handling multipart video decoding and frame buffering); "
        "(2) Preprocessing Tier (executing MTCNN landmark tracking, boundary padding, and affine face alignment); (3) Dual-Branch Feature "
        "Extraction Engine (executing spatial EfficientNet-B4 and spectral 2D-DCT-II in parallel); (4) Attention-Gated Bilinear Fusion Tier "
        "(dynamically weighting inter-domain representations); and (5) Presentation & Governance Tier (Streamlit UI, Plotly gauges, Grad-CAM "
        "heatmaps, and certified audit logging)."
    )

    add_heading_2(doc, "3.4 Design Diagrams")

    add_heading_3(doc, "3.4.1 Data Flow Diagrams")
    add_body_p(
        doc,
        "The data flow within DeepGuard AI is formally modeled across multiple abstraction levels. Figure 3.2 illustrates the Context-Level "
        "(Level 0) DFD, defining the interaction boundaries between the forensic user and the system."
    )

    add_figure(
        doc,
        r'D:\mini-project\SUBMISSION\2_data_flow_diagram_dfd.png',
        caption_text="Context-level (Level 0) Data Flow Diagram illustrating interaction boundaries between the Forensic Examiner and the DeepGuard AI System",
        fig_num="Figure 3.2",
        width_in=5.2
    )

    add_body_p(
        doc,
        "Figure 3.3 illustrates the Level 1 Detailed Forensic Data Flow Diagram, decomposing the system into its five constituent processes: "
        "Video Decoding, Facial Preprocessing, Dual-Stream Inference, Dynamic Attention Gating, and Explainable Forensic Reporting."
    )

    add_figure(
        doc,
        r'D:\mini-project\SUBMISSION\Architecture_Diagram.png',
        caption_text="Level 1 Detailed Forensic Data Flow Diagram showing end-to-end data transformation from raw video stream to calibrated forensic verdict",
        fig_num="Figure 3.3",
        width_in=5.3
    )

    add_heading_3(doc, "3.4.2 Architectural and Use-Case Diagrams")
    add_body_p(
        doc,
        "The internal structure of the dual-stream neural network is illustrated in Figure 3.4. It showcases the exact dimensional transitions "
        "from the 256x256 facial crops to the 1792-d spatial embedding and 512-d spectral embedding."
    )

    add_figure(
        doc,
        r'D:\mini-project\SUBMISSION\3_dual_stream_deep_dive.png',
        caption_text="Dual-Stream Deep Dive Architecture showing decoupled spatial EfficientNet-B4 and spectral 2D-DCT processing branches",
        fig_num="Figure 3.4",
        width_in=5.3
    )

    add_body_p(
        doc,
        "Figure 3.5 provides an architectural close-up of the Attention-Gated Bilinear Fusion Gate mechanism, highlighting the Sigmoid "
        "gating scalar generation that dynamically weighs spatial and spectral representations."
    )

    add_figure(
        doc,
        r'D:\mini-project\SUBMISSION\4_attention_fusion_gate.png',
        caption_text="Attention-Gated Bilinear Fusion Gate mechanism detailing dynamic gating vector generation and dimensional projections",
        fig_num="Figure 3.5",
        width_in=5.2
    )

    add_body_p(
        doc,
        "Figure 3.6 presents the formal Use-Case Diagram for DeepGuard AI, illustrating how Forensic Examiners, Fintech KYC Officers, "
        "and Security Auditors interact with the platform's core operational capabilities."
    )

    add_figure(
        doc,
        r'D:\mini-project\report_assets\fig3_7_use_case_diagram.png',
        caption_text="Use-Case Diagram for Digital Forensic Examination detailing actor roles and verified functional use cases",
        fig_num="Figure 3.6",
        width_in=5.2
    )

    add_heading_2(doc, "3.5 Technology Stack")
    add_body_p(
        doc,
        "The software architecture leverages an integrated, modern Python engineering stack designed for low latency and high scientific fidelity."
    )

    t34_headers = ["Layer", "Technology / Framework", "Specific Version", "Functional Purpose"]
    t34_rows = [
        ["Programming Language", "Python", "3.11 / 3.12 64-bit", "Core application logic and mathematical modeling"],
        ["Deep Learning Engine", "PyTorch (CUDA Enabled)", "2.2.0+", "Tensor computation, GPU acceleration, and autograd"],
        ["Model Library", "timm (PyTorch Image Models)", "0.9.12+", "Pre-trained EfficientNet-B4 backbone architecture"],
        ["Signal Processing", "SciPy (scipy.fftpack)", "1.11.4+", "Orthogonal 2D Discrete Cosine Transform (DCT-II)"],
        ["Computer Vision", "OpenCV (opencv-python)", "4.8.1+", "Video demuxing, temporal frame extraction, and overlays"],
        ["Facial Alignment", "facenet-pytorch (MTCNN)", "2.5.3+", "Multi-task cascaded facial landmark tracking & cropping"],
        ["Explainable AI", "Grad-CAM Implementation", "Custom (torch)", "Spatial and spectral class activation heatmap synthesis"],
        ["Interactive UI", "Streamlit", "1.35.0+", "High-responsiveness reactive forensic examiner web dashboard"],
        ["Visual Telemetry", "Plotly Graph Objects", "5.18.0+", "Interactive confidence gauges and frame probability curves"],
        ["Report Generation", "win32com / python-docx", "3.0.1+", "Automated generation of audit-ready PDF forensic certificates"],
        ["Version Management", "Git & GitHub", "2.40+", "Source code versioning and collaborative repository hosting"]
    ]
    add_table_custom(
        doc, t34_headers, t34_rows,
        caption_text="Technology stack and dependency architectural breakdown",
        table_num="Table 3.4",
        col_widths=[1.2, 1.4, 1.0, 2.1]
    )

    add_heading_2(doc, "3.6 Data Governance, Chain-of-Custody & Forensic Security")
    add_body_p(
        doc,
        "In digital video forensics, evidentiary validity requires strict adherence to legal chain-of-custody protocols. "
        "DeepGuard AI enforces four data governance pillars: "
        "(1) Non-Destructive Ingestion: Input video files are accessed via read-only memory streams, ensuring original media bits are "
        "never altered or re-encoded during processing; "
        "(2) Cryptographic Evidence Hashing: Upon upload, the system computes the SHA-256 cryptographic digest of the raw video file. "
        "This hash is embedded within all output forensic certificates, providing immutable proof of evidence integrity; "
        "(3) Ephemeral Data Retention: To comply with biometric privacy standards (including GDPR and Indian Digital Personal Data "
        "Protection Act), extracted facial crops and intermediate tensor caches are automatically purged from system memory upon session "
        "termination; and "
        "(4) Verifiable Audit Trails: All model decisions, intermediate attention gate scalars, frame timestamps, and confidence percentages "
        "are serialized into standardized JSON forensic logs for third-party judicial audit."
    )

    add_heading_2(doc, "3.7 Use-Case Walkthroughs and Requirement Traceability")
    add_body_p(
        doc,
        "A typical forensic verification workflow proceeds through an orchestrated sequence: "
        "First, the examiner uploads a suspect digital recording (e.g., MP4 format). The system validates video headers and computes the "
        "SHA-256 evidence hash. Next, the video processor extracts sequential frames at 5 FPS and passes them to MTCNN, which isolates "
        "canonical 256x256 face crops with a 15% contextual boundary margin. In the dual-stream inference phase, the spatial branch "
        "evaluates pixel texture anomalies while the frequency branch computes 2D-DCT spectral coefficients. The attention gate combines "
        "these embeddings to yield a calibrated real-versus-fake probability. Finally, Grad-CAM overlays and Plotly temporal trajectories "
        "are rendered on the dashboard, and a certified PDF report is compiled for forensic submission. Every step maps directly to FR1–FR13."
    )

    add_heading_2(doc, "3.8 Risk Analysis and Mitigation Strategies")
    add_body_p(
        doc,
        "Operational risks and engineering mitigations are outlined below:"
    )
    add_bullet_p(
        doc,
        "Extreme Video Compression Noise: Heavy social media re-encoding (c40 tier) obliterates high-frequency facial gradients. "
        "Mitigation: The frequency stream analyzes low-to-mid frequency DCT coefficients and radial rings, which resist compression artifacts, "
        "while the attention gate automatically shifts weighting away from the degraded spatial stream."
    )
    add_bullet_p(
        doc,
        "Adversarial Noise and Post-Processing Perturbations: Generative tools frequently apply Gaussian blurring or sharpening to mask "
        "deepfake seams. Mitigation: Extensive data augmentation during training (random JPEG compression Q∈[40,90], Gaussian blur σ∈[0.1,2.0], "
        "and color jittering) ensures invariant feature representations."
    )
    add_bullet_p(
        doc,
        "Motion Blur and Low-Light Occlusion: Fast camera movement can cause MTCNN to miss faces. Mitigation: Temporal frame interpolation "
        "and fallback crop tracking ensure continuous forensic telemetry across the video duration."
    )

    add_heading_2(doc, "3.9 Quality Attributes and Design Constraints")
    add_body_p(
        doc,
        "The architecture is constrained by three essential quality attributes: "
        "(1) Latency Guarantee: To allow integration into automated KYC verification gates, inference must execute in real time (< 50ms/frame); "
        "(2) Explainability Requirement: No classification may be presented without accompanying spatial and frequency Grad-CAM heatmaps; and "
        "(3) Resource Constrained Deployment: Total model size must remain under 25 million parameters to enable deployment on edge forensics "
        "laptops and workstations lacking high-end enterprise GPU clusters."
    )

    doc.add_page_break()
