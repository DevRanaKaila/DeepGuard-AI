from build_report.helpers import (
    add_heading_1, add_heading_2, add_heading_3, add_body_p, add_bullet_p
)

def add_chapter_7(doc):
    add_heading_1(doc, "CHAPTER 7: CONCLUSION AND FUTURE SCOPE")

    add_body_p(
        doc,
        "This concluding chapter synthesizes the primary research contributions of the DeepGuard AI project, critically evaluates "
        "identified technical limitations, delineates prospective future research directions, proposes a structured institutional and "
        "industrial adoption framework, and details a prioritized engineering roadmap."
    )

    add_heading_2(doc, "7.1 Conclusion")
    add_body_p(
        doc,
        "This project successfully designed, implemented, evaluated, and deployed DeepGuard AI: a robust, dual-stream deep learning "
        "forensic system engineered to detect facial manipulation in digital video sequences. By systematically investigating and overcoming "
        "the fatal vulnerability of conventional single-stream models—their severe degradation under real-world video compression—DeepGuard "
        "AI couples the semantic representational power of an EfficientNet-B4 spatial convolutional network with the mathematical invariance "
        "of 2D Discrete Cosine Transform (DCT-II) spectral analysis."
    )
    add_body_p(
        doc,
        "Through the formulation of the Radial Azimuthal Spectrum A(r) and an Attention-Gated Bilinear Fusion mechanism, the architecture "
        "dynamically adapts to varying transmission compression levels, shifting evidential trust to the frequency stream when video "
        "compression obliterates pixel-level gradients. Rigorous empirical benchmarking across FaceForensics++ (raw, c23, c40) and Celeb-DF v2 "
        "demonstrated that DeepGuard AI achieves 98.9% raw accuracy, maintains 94.2% accuracy on c23 compression, achieves 89.6% on heavy c40 "
        "compression, and delivers a superior cross-dataset AUC-ROC of 0.968. By integrating dual-stream Grad-CAM explainability and an "
        "interactive Streamlit forensic dashboard, the system effectively bridges the gap between academic computer vision research and "
        "high-assurance forensic deployment."
    )

    add_heading_2(doc, "7.2 Identified Limitations")
    add_body_p(
        doc,
        "Despite its significant advances, three technical boundaries and operational limitations are acknowledged:"
    )
    add_bullet_p(
        doc,
        "Facial-Centric Visual Boundary: The current implementation focuses exclusively on facial crops extracted by MTCNN. Full-body "
        "neural synthesis, deepfake voice cloning (audio forensics), and background environment manipulation remain outside the detection scope."
    )
    add_bullet_p(
        doc,
        "Computational Memory Constraints during Batch Video Ingestion: Processing high-definition (1080p/4K) video streams at high frame "
        "rates requires substantial GPU memory. On edge devices lacking dedicated VRAM, frame sampling must be throttled to 5 FPS to "
        "prevent out-of-memory exceptions."
    )
    add_bullet_p(
        doc,
        "Diffusion Model Generalization: While 2D-DCT spectral profiling reliably detects transposed convolution checkerboard artifacts "
        "inherent in GAN architectures, emerging text-to-video diffusion frameworks (e.g., OpenAI Sora, Runway Gen-2) rely on patch-based "
        "diffusion transformers that produce subtly different spectral distributions requiring specialized retraining."
    )

    add_heading_2(doc, "7.3 Future Scope and Technical Roadmap")
    add_body_p(
        doc,
        "To advance the forensic capabilities of DeepGuard AI, four key research directions are prioritized:"
    )
    add_bullet_p(
        doc,
        "1. Audio-Visual Cross-Modal Synchronization: Integrating acoustic speech prosody features (via OpenAI Whisper or wav2vec 2.0) "
        "with visual lip-motion vectors to detect subtle temporal desynchronization between spoken phonemes and visual visemes."
    )
    add_bullet_p(
        doc,
        "2. Temporal Attention Modeling via Video Transformers: Augmenting frame-level predictions with TimeSformer or Video Vision "
        "Transformers (ViViT) to model inter-frame biological cadence, such as unnatural blinking frequencies and micro-expression anomalies."
    )
    add_bullet_p(
        doc,
        "3. Edge Optimization via TensorRT and ONNX Runtime: Quantizing model weights to INT8 precision using NVIDIA TensorRT to enable "
        "real-time (< 15ms) inference on low-power edge surveillance cameras, mobile devices, and automated border control kiosks."
    )
    add_bullet_p(
        doc,
        "4. Diffusion-Specific Spectral Forensics: Extending the frequency stream to model the unique high-frequency noise residuals "
        "characteristic of iterative denoising diffusion probabilistic models (DDPMs)."
    )

    add_heading_2(doc, "7.4 Adoption, Maintenance, and Forensic Rollout Plan")
    add_body_p(
        doc,
        "A structured rollout methodology is recommended for enterprise deployment: "
        "(1) Phase I (Pilot Integration): Deploy DeepGuard AI alongside existing manual KYC verification queues in fintech onboarding, "
        "operating in shadow-monitoring mode to collect baseline operational telemetry; "
        "(2) Phase II (Examiner Certification): Train digital forensic examiners to interpret dual Grad-CAM heatmaps and Radial Azimuthal "
        "profiles, establishing standard operating procedures (SOPs) for judicial testimony; and "
        "(3) Phase III (Automated Enforcement): Integrate the RESTful FastAPI inference endpoints directly into automated KYC gating systems, "
        "enabling real-time rejection of synthetic facial attacks with automated cryptographic certificate generation."
    )

    add_heading_2(doc, "7.5 Prioritised Future Engineering Roadmap")
    add_body_p(
        doc,
        "The post-submission engineering roadmap is structured into three milestones: "
        "Milestone 1 (Months 1–3): Package the deep learning engine as an optimized Docker container with ONNX Runtime GPU acceleration; "
        "Milestone 2 (Months 4–6): Implement multi-face tracking for multi-subject group videos and crowd forensic analysis; "
        "Milestone 3 (Months 7–12): Submit the dual-stream architecture, empirical benchmarks, and spectral theory to a Scopus/IEEE indexed "
        "international journal on information forensics and cybersecurity."
    )

    doc.add_page_break()
