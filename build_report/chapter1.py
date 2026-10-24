from build_report.helpers import (
    add_heading_1, add_heading_2, add_heading_3, add_body_p, add_bullet_p
)

def add_chapter_1(doc):
    add_heading_1(doc, "CHAPTER 1: INTRODUCTION")

    add_heading_2(doc, "1.1 Background and Societal Context")
    add_body_p(
        doc,
        "The contemporary digital communications landscape has been fundamentally reshaped by exponential breakthroughs "
        "in deep generative modeling. Over the past five years, the evolution of Generative Adversarial Networks (GANs), "
        "Variational Autoencoders (VAEs), and Latent Diffusion Models (LDMs) has democratized the synthesis of hyper-realistic "
        "digital media. Open-source facial manipulation toolsets such as DeepFaceLab, FaceSwap, SimSwap, and modern text-to-video "
        "diffusion pipelines now allow individuals without specialized computer graphics knowledge to manipulate facial identities, "
        "fabricate emotional expressions, and synchronize lip movements with synthesized audio in ultra-high resolution. These manipulated "
        "visual sequences are widely referred to as deepfakes."
    )
    add_body_p(
        doc,
        "While deep synthesis techniques offer legitimate creative utility across motion picture production, digital education, "
        "accessible avatar design, and virtual telepresence, their unauthorized weaponization poses an unprecedented existential threat "
        "to societal trust, democratic integrity, and digital security. Deepfakes have emerged as potent instruments of sophisticated "
        "social engineering, political disinformation, corporate wire fraud, automated KYC (Know Your Customer) bypass attacks in "
        "fintech platforms, and targeted non-consensual defamation. As generative decoders increasingly mimic natural optical textures, "
        "the human perceptual visual system is rendered incapable of discerning authentic recordings from synthetic fabrications, "
        "reducing manual detection accuracy to near-random chance."
    )
    add_body_p(
        doc,
        "The urgency of establishing reliable digital forensics is heightened by the velocity and scale of social media diffusion. "
        "Modern content distribution networks compress, downsample, and transmit video streams across millions of devices in seconds. "
        "In this high-velocity environment, malicious deepfake videos can alter electoral consensus, spark civil unrest, or induce severe "
        "financial market volatility before traditional human fact-checkers can even initiate verification. Consequently, the development "
        "of automated, mathematically grounded, compression-resilient, and forensically explainable deep learning detection systems has "
        "become an urgent priority for modern computer science and cybersecurity."
    )

    add_heading_2(doc, "1.2 Problem Statement")
    add_body_p(
        doc,
        "Current digital video forensic systems exhibit severe operational vulnerabilities when deployed outside controlled "
        "laboratory environments. Existing deepfake detection research suffers from four fundamental bottlenecks:"
    )
    add_bullet_p(
        doc,
        "Spatial-Domain Compression Vulnerability: Conventional detection models rely predominantly on RGB spatial convolutional "
        "neural networks (e.g., standard ResNet, VGG, or XceptionNet baselines) that attempt to identify localized visual flaws such "
        "as boundary blending, skin warping, or lighting inconsistencies. However, when videos undergo standard lossy social media "
        "compression (H.264/H.265 codecs, downsampling, and color quantization), subtle pixel-level gradient artifacts are destroyed. "
        "As a result, spatial-only detectors experience catastrophic performance drops of 20% to 35% in accuracy when transitioning "
        "from raw uncompressed video to high-compression transmission tiers (such as FaceForensics++ c40)."
    )
    add_bullet_p(
        doc,
        "Absence of Systematic Spectral Fingerprinting: Generative decoders universally employ transposed convolutions or nearest-neighbor "
        "upsampling layers to reconstruct high-resolution facial images from latent vectors. Signal processing theory establishes that "
        "these upsampling operators leave indelible, periodic grid artifacts and high-frequency discrepancies in the frequency domain. "
        "Despite this, competition-grade winning architectures—including the 1st-place Kaggle DFDC solution—operate entirely in the spatial "
        "domain, completely discarding the rich discriminative signal available in orthogonal frequency transforms."
    )
    add_bullet_p(
        doc,
        "Forensic Opacity and the Black-Box Problem: Deployed deepfake classifiers overwhelmingly function as opaque mathematical black "
        "boxes that produce an isolated scalar probability score. Without visual attribution demonstrating which specific facial features "
        "or spectral frequency bands triggered the classification, such models fail the evidentiary standards required for courtroom "
        "admissibility, regulatory reporting, and legal compliance."
    )
    add_bullet_p(
        doc,
        "Deployment and Usability Gap: Research-grade detection algorithms typically exist as isolated, non-standardized Python command-line "
        "scripts that require deep technical expertise to configure, preprocess, and execute. Non-expert stakeholders—including forensic "
        "investigators, compliance officers, and journalists—lack access to interactive, intuitive forensic dashboards capable of real-time "
        "video ingestion, multi-modal explainability, and automated verification reporting."
    )
    add_body_p(
        doc,
        "To resolve these interrelated challenges, this project formulates and implements DeepGuard AI: a unified dual-stream forensic "
        "framework that harmonizes spatial semantic feature extraction (via EfficientNet-B4) with orthogonal 2D Discrete Cosine Transform "
        "(DCT-II) frequency analysis through an attention-gated bilinear fusion mechanism, providing verifiable Grad-CAM explainability "
        "and a production-ready interactive web dashboard."
    )

    add_heading_2(doc, "1.3 Objectives of the Project")
    add_body_p(
        doc,
        "The primary objective of this project is to architect, evaluate, and deploy a robust, compression-resilient, and "
        "interpretable deepfake video detection system. The specific technical objectives are as follows:"
    )
    add_bullet_p(
        doc,
        "Automated Video Preprocessing & Facial Tracking: To implement a robust video demuxing and frame extraction pipeline that "
        "samples frames at a uniform temporal rate (5 FPS) and applies Multi-task Cascaded Convolutional Networks (MTCNN) to automatically "
        "detect facial landmarks, execute canonical alignment, and crop facial regions with a 15% contextual boundary margin to capture "
        "peripheral blending seams."
    )
    add_bullet_p(
        doc,
        "Frequency-Domain Spectral Artifact Extraction: To mathematically formulate and implement an orthogonal 2D Discrete Cosine "
        "Transform (DCT-II) module with logarithmic scaling and 1D Radial Azimuthal Spectrum pooling A(r) to extract rotationally invariant "
        "fingerprints of GAN upsampling operations."
    )
    add_bullet_p(
        doc,
        "Dual-Branch Neural Network Architecture: To engineer a decoupled deep neural architecture comprising (a) an EfficientNet-B4 "
        "spatial backbone extracting a 1792-dimensional semantic visual embedding, and (b) a 4-stage custom Spectral-CNN extracting a "
        "512-dimensional frequency embedding."
    )
    add_bullet_p(
        doc,
        "Attention-Gated Bilinear Feature Fusion: To develop a learnable gating mechanism that dynamically evaluates the compression "
        "context of the input frame, assigning adaptive weights to the spatial and frequency streams prior to classification."
    )
    add_bullet_p(
        doc,
        "Forensic Interpretability via Grad-CAM: To incorporate Gradient-weighted Class Activation Mapping across both spatial and spectral "
        "layers, generating dual-domain heatmaps that highlight the exact facial anatomy and frequency bands responsible for the verdict."
    )
    add_bullet_p(
        doc,
        "Interactive Forensic Dashboard & Automated Reporting: To design and deploy a full-featured Streamlit web application providing "
        "drag-and-drop video upload, real-time probability meters, frame-by-frame temporal trajectory analysis, and downloadable PDF forensic "
        "certificates."
    )

    add_heading_2(doc, "1.4 Scope of the Project")
    add_body_p(
        doc,
        "The scope of DeepGuard AI covers the complete digital forensic verification lifecycle for facial manipulation in video sequences. "
        "Specifically, the project addresses four major manipulation paradigms defined in the benchmark FaceForensics++ repository: "
        "(1) Deepfakes (autoencoder-based identity replacement), (2) Face2Face (computer-graphics-based facial expression reenactment), "
        "(3) FaceSwap (graphics-based face replacement with boundary blending), and (4) NeuralTextures (neural rendering-based mouth and "
        "facial reenactment). The system evaluates both uncompressed raw media and compressed video tiers (c23 light compression and c40 "
        "heavy compression) to ensure practical applicability to social media video transmission."
    )
    add_body_p(
        doc,
        "The system processes digital video formats including MP4, AVI, MOV, and MKV. Analysis is conducted at the frame level and "
        "aggregated across the temporal dimension to produce calibrated video-level authenticity verdicts. The project strictly focuses "
        "on visual and spectral forensics within facial regions; audio-stream spoofing detection, physiological biosignal tracking "
        "(e.g., remote photoplethysmography), and text metadata provenance analysis remain outside the primary boundary of this work, "
        "allowing dedicated computational optimization of the dual-stream computer vision pipeline."
    )

    add_heading_2(doc, "1.5 Stakeholder Needs and Operating Assumptions")
    add_body_p(
        doc,
        "DeepGuard AI addresses the operational requirements of three primary stakeholder groups:"
    )
    add_bullet_p(
        doc,
        "Digital Forensic Examiners and Law Enforcement: Investigators require mathematically verifiable forensic tools capable of "
        "ingesting suspect video evidence, generating tamper heatmaps that isolate manipulated facial landmarks, and producing audit-ready "
        "evidentiary reports admissible in judicial proceedings."
    )
    add_bullet_p(
        doc,
        "Financial Technology (Fintech) and KYC Compliance Officers: Automated identity verification pipelines in banking and cryptocurrency "
        "exchanges require ultra-low latency (< 50ms/frame) inference to defend biometric onboarding against video replay and digital identity "
        "spoofing attacks."
    )
    add_bullet_p(
        doc,
        "Social Media Platforms and Media Fact-Checkers: Content moderation teams require scalable, compression-resilient detection "
        "engines that maintain high accuracy even after media has undergone multiple re-encoding passes on platforms such as WhatsApp or YouTube."
    )
    add_body_p(
        doc,
        "Operating assumptions include: (a) input video streams contain recognizable human facial sequences suitable for tracking by MTCNN; "
        "(b) video resolution is at least 360p (480x360 pixels) to permit canonical 256x256 face crop extraction; and (c) the host system "
        "provides standard Python execution capabilities with optional CUDA hardware acceleration for high-throughput batch evaluation."
    )

    add_heading_2(doc, "1.6 Organisation of the Report")
    add_body_p(
        doc,
        "The remainder of this report is organized into six technical chapters and supporting documentation: "
        "Chapter 2 reviews the theoretical foundations of deepfake generation, existing spatial and frequency detection architectures, "
        "and identifies the key research gaps motivating our dual-stream approach. "
        "Chapter 3 presents the requirement specifications, feasibility analysis, system architecture, data flow diagrams (Level 0 and Level 1), "
        "use-case models, and data governance frameworks. "
        "Chapter 4 provides a granular description of the implementation, including mathematical formulations of the 2D-DCT-II and Radial "
        "Azimuthal Spectrum A(r), the EfficientNet-B4 spatial backbone, attention-gated bilinear fusion, code snippets, and UI screenshots. "
        "Chapter 5 details the verification strategy, test case execution (TC1 to TC18), automated test suite results, and forensic validity. "
        "Chapter 6 presents empirical results, benchmark comparisons on FaceForensics++ and Celeb-DF v2, ROC curves, confusion matrices, and "
        "operational discussion. "
        "Chapter 7 concludes the report with operational rollout guidelines and future research directions. "
        "References and Appendices containing source code extracts and deployment metadata conclude the document."
    )

    doc.add_page_break()
