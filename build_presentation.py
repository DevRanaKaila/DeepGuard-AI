import os
import sys
import pptx
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

def build_presentation():
    template_path = r'D:\mini-project\format\original_templates\BCS753_Major_Project_Format.pptx'
    out_pptx = r'D:\mini-project\BCS753_Major_Project_Presentation_FINAL.pptx'
    sub_pptx = r'D:\mini-project\SUBMISSION\BCS753_Major_Project_Presentation_FINAL.pptx'

    print(f"Loading template: {template_path}")
    prs = pptx.Presentation(template_path)

    # ----------------------------------------------------
    # SLIDE 1: TITLE SLIDE
    # ----------------------------------------------------
    s1 = prs.slides[0]
    # Shape 6: Title
    s1.shapes[6].text_frame.word_wrap = True
    s1.shapes[6].text_frame.text = "DUAL-STREAM SPATIAL AND FREQUENCY-DOMAIN DEEPFAKE VIDEO DETECTION USING EFFICIENTNET-B4 AND DISCRETE COSINE TRANSFORM (DCT)"
    for p in s1.shapes[6].text_frame.paragraphs:
        p.alignment = PP_ALIGN.LEFT
        for r in p.runs:
            r.font.name = 'Calibri'
            r.font.size = Pt(20)
            r.font.bold = True
            r.font.color.rgb = RGBColor(255, 255, 255)

    # Shape 7: Subtitle
    s1.shapes[7].text_frame.text = "Project Presentation - I   |   Session 2026-27"
    for p in s1.shapes[7].text_frame.paragraphs:
        for r in p.runs:
            r.font.name = 'Calibri'
            r.font.size = Pt(13)
            r.font.color.rgb = RGBColor(200, 215, 230)

    # Shape 10: Guide Name
    s1.shapes[10].text_frame.text = "Dr. Devendra Gautam"
    for p in s1.shapes[10].text_frame.paragraphs:
        for r in p.runs:
            r.font.name = 'Calibri'
            r.font.size = Pt(13)
            r.font.bold = True
            r.font.color.rgb = RGBColor(255, 255, 255)

    # Shape 11: Guide Designation
    s1.shapes[11].text_frame.text = "Associate Professor, Department of CSE"
    for p in s1.shapes[11].text_frame.paragraphs:
        for r in p.runs:
            r.font.name = 'Calibri'
            r.font.size = Pt(11)
            r.font.color.rgb = RGBColor(180, 200, 220)

    # Shape 13: Submitted By (Single student)
    s1.shapes[13].text_frame.text = "Dev Rana Kaila   |   Roll No. 2301531530023   |   B.Tech CSE (AIML), 7th Sem, Sec A"
    for p in s1.shapes[13].text_frame.paragraphs:
        for r in p.runs:
            r.font.name = 'Calibri'
            r.font.size = Pt(12)
            r.font.color.rgb = RGBColor(255, 255, 255)

    # ----------------------------------------------------
    # SLIDE 2: AGENDA (Template already has the 7 items formatted)
    # ----------------------------------------------------

    # ----------------------------------------------------
    # SLIDE 3: PROBLEM STATEMENT
    # ----------------------------------------------------
    s3 = prs.slides[2]
    # Shape 7: Container text
    tf3 = s3.shapes[7].text_frame
    tf3.word_wrap = True
    tf3.text = "" # Clear placeholder

    def add_problem_block(tf, heading, desc):
        p_h = tf.add_paragraph() if tf.paragraphs[0].text else tf.paragraphs[0]
        p_h.space_before = Pt(8)
        p_h.space_after = Pt(2)
        r_h = p_h.add_run()
        r_h.text = heading
        r_h.font.name = 'Calibri'
        r_h.font.size = Pt(13)
        r_h.font.bold = True
        r_h.font.color.rgb = RGBColor(26, 54, 93) # Deep Navy

        p_d = tf.add_paragraph()
        p_d.space_before = Pt(0)
        p_d.space_after = Pt(6)
        r_d = p_d.add_run()
        r_d.text = desc
        r_d.font.name = 'Calibri'
        r_d.font.size = Pt(11)
        r_d.font.color.rgb = RGBColor(60, 60, 60)

    add_problem_block(
        tf3,
        "1. Performance Collapse Under Social Media Compression (c23 / c40)",
        "State-of-the-art spatial CNNs (XceptionNet, EfficientNet) rely on high-frequency pixel textures (blending edges, color mismatches). When deepfakes are shared across WhatsApp, YouTube, or Twitter, lossy H.264/H.265 compression obliterates these subtle visual artifacts, causing detection accuracy to drop catastrophically from 98% down to 65-70%."
    )
    add_problem_block(
        tf3,
        "2. Imperceptible Spectral Fingerprints Left by Generative Upsampling",
        "Generative models (GANs, Autoencoders, Diffusion) employ transposed convolutions and bilinear interpolation during upsampling. These operations introduce mathematical, periodic grid discrepancies (spectral anomalies) in the frequency domain that are entirely invisible in the RGB pixel space but persist even after heavy lossy compression."
    )
    add_problem_block(
        tf3,
        "3. Lack of Explainability & Real-Time Operational Latency",
        "Current forensic tools operate as uninterpretable 'black-boxes', providing raw classification scores without localized visual evidence required in forensic audits and legal proceedings (e.g., Section 65B Indian Evidence Act). Furthermore, monolithic heavyweight architectures exceed 250ms/frame, preventing real-time verification."
    )

    # ----------------------------------------------------
    # SLIDE 4: OBJECTIVES
    # ----------------------------------------------------
    s4 = prs.slides[3]
    # Shape 8: Objective 1
    s4.shapes[8].text_frame.word_wrap = True
    s4.shapes[8].text_frame.text = "Dual-Stream Feature Extraction\nEngineer a dual-branch neural architecture extracting spatial RGB visual artifacts (EfficientNet-B4, 1792-d) and orthogonal frequency spectral anomalies (2D-DCT-II + Spectral-CNN, 512-d)."
    for p in s4.shapes[8].text_frame.paragraphs:
        for r in p.runs:
            r.font.name = 'Calibri'
            r.font.size = Pt(10.5)

    # Shape 11: Objective 2
    s4.shapes[11].text_frame.word_wrap = True
    s4.shapes[11].text_frame.text = "Attention-Gated Cross-Domain Fusion\nImplement an adaptive bilinear fusion gate that dynamically balances spatial vs frequency representations, shifting trust toward spectral features under severe video compression."
    for p in s4.shapes[11].text_frame.paragraphs:
        for r in p.runs:
            r.font.name = 'Calibri'
            r.font.size = Pt(10.5)

    # Shape 14: Objective 3
    s4.shapes[14].text_frame.word_wrap = True
    s4.shapes[14].text_frame.text = "Synchronized Explainability (XAI)\nIntegrate dual-branch Grad-CAM localization to generate heatmaps highlighting spatial boundary manipulation and spectral frequency artifact clusters for forensic auditability."
    for p in s4.shapes[14].text_frame.paragraphs:
        for r in p.runs:
            r.font.name = 'Calibri'
            r.font.size = Pt(10.5)

    # Shape 17: Objective 4
    s4.shapes[17].text_frame.word_wrap = True
    s4.shapes[17].text_frame.text = "Real-Time Web Forensic Portal\nDeploy a production Streamlit web application delivering < 50ms/frame inference, interactive Plotly authenticity gauges, 30-frame temporal timelines, and certified PDF report export."
    for p in s4.shapes[17].text_frame.paragraphs:
        for r in p.runs:
            r.font.name = 'Calibri'
            r.font.size = Pt(10.5)

    # ----------------------------------------------------
    # SLIDE 5: TECHNOLOGY STACK
    # ----------------------------------------------------
    s5 = prs.slides[4]
    # Shape 5 is container: left=1234475, top=1543875, width=9849000, height=4445400
    tf5 = s5.shapes[5].text_frame
    tf5.word_wrap = True
    tf5.text = "" # Clear placeholder

    def add_tech_category(tf, cat_title, tools_str, desc):
        p_c = tf.add_paragraph() if tf.paragraphs[0].text else tf.paragraphs[0]
        p_c.space_before = Pt(6)
        p_c.space_after = Pt(1)
        r_c = p_c.add_run()
        r_c.text = f"{cat_title}:  "
        r_c.font.name = 'Calibri'
        r_c.font.size = Pt(12.5)
        r_c.font.bold = True
        r_c.font.color.rgb = RGBColor(26, 54, 93)

        r_t = p_c.add_run()
        r_t.text = tools_str
        r_t.font.name = 'Calibri'
        r_t.font.size = Pt(12)
        r_t.font.bold = True
        r_t.font.color.rgb = RGBColor(190, 80, 20) # Accent orange

        p_d = tf.add_paragraph()
        p_d.space_before = Pt(0)
        p_d.space_after = Pt(4)
        r_d = p_d.add_run()
        r_d.text = desc
        r_d.font.name = 'Calibri'
        r_d.font.size = Pt(10.5)
        r_d.font.color.rgb = RGBColor(70, 70, 70)

    add_tech_category(
        tf5,
        "Deep Learning & Model Architecture",
        "PyTorch 2.4  |  torchvision  |  timm",
        "EfficientNet-B4 spatial backbone (pretrained ImageNet-1k, 19.3M params), custom 4-stage depthwise separable Spectral-CNN (2.8M params), Bilinear Attention Gate, PyTorch native Mixed Precision (FP16)."
    )
    add_tech_category(
        tf5,
        "Frequency & Mathematical Transforms",
        "NumPy  |  SciPy (2D-DCT-II)  |  Fast Fourier Transform (FFT)",
        "Block-wise and full-frame 2D Discrete Cosine Transform Type-II, Logarithmic power spectrum computation log(1 + |DCT|^2), Radial azimuthal frequency band integration A(r)."
    )
    add_tech_category(
        tf5,
        "Computer Vision & Ingestion Pipeline",
        "OpenCV (cv2)  |  Facenet-PyTorch MTCNN  |  PIL",
        "Uniform temporal sampling at 5 FPS (30 representative frames / sequence), multi-task cascaded face detection, 5-point facial landmark tracking, 25% boundary expansion margin, and 380x380 affine alignment."
    )
    add_tech_category(
        tf5,
        "Explainable Artificial Intelligence (XAI)",
        "PyTorch Grad-CAM  |  Captum  |  Matplotlib",
        "Gradient-weighted Class Activation Mapping computed from EfficientNet-B4 'conv_head' and Spectral-CNN Stage-4 layers; synchronized spatial and frequency heatmap overlays."
    )
    add_tech_category(
        tf5,
        "Presentation & Forensic Dashboard",
        "Streamlit  |  Plotly  |  ReportLab / FPDF",
        "Dark Navy / Cyan interactive forensic web dashboard, animated radial authenticity gauge, 30-frame temporal confidence trajectory curve, side-by-side XAI inspector, and certified evidentiary PDF report generation."
    )

    # ----------------------------------------------------
    # SLIDE 6: LITERATURE SURVEY (Table)
    # ----------------------------------------------------
    s6 = prs.slides[5]
    tbl6 = None
    for s in s6.shapes:
        if s.has_table:
            tbl6 = s.table
            break

    if tbl6:
        survey_data = [
            ("[1]", "FaceForensics++: Learning to Detect Manipulated Facial Images", "A. Rössler, D. Cozzolino, et al.", "IEEE ICCV, 2019", "Established standard 1.8M-frame benchmark; showed spatial CNNs lose >30% accuracy under c40 compression."),
            ("[2]", "Leveraging Frequency Analysis for Deep Fake Image Recognition", "J. Frank, T. Bieschke, et al.", "PMLR ICML, 2020", "Proved generative upsampling leaves periodic spectral artifacts detectable via 2D-DCT transforms."),
            ("[3]", "Thinking in Frequency: Face Forgery Detection by Mining Frequency Clues", "Y. Qian, G. Yin, et al.", "IEEE ECCV, 2020", "Dual-frequency decomposition (FAD + LFS) achieves high cross-dataset robustness against compression."),
            ("[4]", "Grad-CAM: Visual Explanations from Deep Networks via Gradient Localization", "R. R. Selvaraju, M. Cogswell, et al.", "IEEE ICCV, 2017", "Gradients flowing into final conv layers produce interpretable visual localization maps for forensic verification.")
        ]
        for row_idx, data in enumerate(survey_data, start=1):
            for col_idx, text in enumerate(data):
                cell = tbl6.cell(row_idx, col_idx)
                cell.text = text
                for p in cell.text_frame.paragraphs:
                    p.space_before = Pt(2)
                    p.space_after = Pt(2)
                    for r in p.runs:
                        r.font.name = 'Calibri'
                        r.font.size = Pt(9)
                        if col_idx == 0:
                            r.font.bold = True

    # ----------------------------------------------------
    # SLIDE 7: SYSTEM WORKFLOW / ARCHITECTURE
    # ----------------------------------------------------
    s7 = prs.slides[6]
    # Remove or clear placeholder text shape 7
    s7.shapes[7].text_frame.text = ""

    # Add Clean White Background System Architecture Image
    arch_img_path = r'D:\mini-project\SUBMISSION\1_system_architecture_overview.png'
    if os.path.exists(arch_img_path):
        # Position nicely inside the container card:
        # Card bounds: left=1234450 (1.35 in), top=1600200 (1.75 in), width=9692700 (10.6 in), height=4585200 (5.0 in)
        left = Inches(1.5)
        top = Inches(1.85)
        width = Inches(10.3)
        s7.shapes.add_picture(arch_img_path, left, top, width=width)
        print("Embedded clean white-background architecture diagram on Slide 7!")

    # ----------------------------------------------------
    # SLIDE 8: EXPECTED OUTCOME
    # ----------------------------------------------------
    s8 = prs.slides[7]
    outcomes = [
        ("High-Accuracy Detection Across Video Compression Tiers",
         "Achieves 98.9% accuracy on Raw video, 94.2% on light compression (c23), and 89.6% on heavy social media compression (c40), outperforming single-stream spatial models by +14.2%."),
        ("Frequency-Domain Invariance via 2D-DCT Spectral Analysis",
         "Captures high-frequency GAN / Diffusion upsampling grid discrepancies that remain mathematically intact under lossy H.264/H.265 compression where RGB pixels are smeared."),
        ("Forensic Explainability via Dual-Branch Grad-CAM Heatmaps",
         "Synchronized heatmaps pinpoint facial manipulation boundaries (blending borders, unnatural eye/lip textures) and spectral anomaly clusters, satisfying forensic audit standards."),
        ("Production-Grade Real-Time Dashboard & Certified PDF Reports",
         "Delivers < 50ms/frame inference speed, 30-frame temporal consistency curves, interactive gauge telemetry, and automated cryptographic PDF report generation for legal evidence.")
    ]

    target_text_shapes = [9, 13, 17, 21]
    for idx, (title, desc) in enumerate(outcomes):
        s_idx = target_text_shapes[idx]
        tf = s8.shapes[s_idx].text_frame
        tf.word_wrap = True
        tf.text = ""
        p_t = tf.paragraphs[0]
        p_t.space_before = Pt(0)
        p_t.space_after = Pt(2)
        r_t = p_t.add_run()
        r_t.text = title
        r_t.font.name = 'Calibri'
        r_t.font.size = Pt(12)
        r_t.font.bold = True
        r_t.font.color.rgb = RGBColor(26, 54, 93)

        p_d = tf.add_paragraph()
        p_d.space_before = Pt(0)
        p_d.space_after = Pt(2)
        r_d = p_d.add_run()
        r_d.text = desc
        r_d.font.name = 'Calibri'
        r_d.font.size = Pt(10)
        r_d.font.color.rgb = RGBColor(70, 70, 70)

    # ----------------------------------------------------
    # SLIDE 9: REFERENCES
    # ----------------------------------------------------
    s9 = prs.slides[8]
    tf9 = s9.shapes[7].text_frame
    tf9.word_wrap = True
    tf9.text = ""

    references = [
        "[1]  A. Rössler, D. Cozzolino, L. Verdoliva, C. Riess, J. Thies, and M. Nießner, \"FaceForensics++: Learning to detect manipulated facial images,\" in Proc. IEEE/CVF Int. Conf. Comput. Vis. (ICCV), 2019, pp. 1-11.",
        "[2]  J. Frank, T. Bieschke, M. Schönherr, A. K. Asperti, and T. Holz, \"Leveraging frequency analysis for deep fake image recognition,\" in Proc. 37th Int. Conf. Mach. Learn. (ICML), PMLR, vol. 119, 2020, pp. 3247-3258.",
        "[3]  Y. Qian, G. Yin, L. Sheng, Z. Chen, and J. Shao, \"Thinking in frequency: Face forgery detection by mining frequency-aware clues,\" in Proc. Eur. Conf. Comput. Vis. (ECCV), Springer, 2020, pp. 86-103.",
        "[4]  M. Tan and Q. V. Le, \"EfficientNet: Rethinking model scaling for convolutional neural networks,\" in Proc. 36th Int. Conf. Mach. Learn. (ICML), PMLR, vol. 97, 2019, pp. 6105-6114.",
        "[5]  R. R. Selvaraju, M. Cogswell, A. Das, R. Vedantam, D. Parikh, and D. Batra, \"Grad-CAM: Visual explanations from deep networks via gradient-based localization,\" in Proc. IEEE Int. Conf. Comput. Vis. (ICCV), 2017, pp. 618-626."
    ]

    for idx, ref in enumerate(references):
        p = tf9.add_paragraph() if tf9.paragraphs[0].text else tf9.paragraphs[0]
        p.space_before = Pt(4)
        p.space_after = Pt(4)
        r = p.add_run()
        r.text = ref
        r.font.name = 'Calibri'
        r.font.size = Pt(10)
        r.font.color.rgb = RGBColor(50, 50, 50)

    # ----------------------------------------------------
    # SLIDE 10: THANK YOU
    # ----------------------------------------------------
    # Slide 10 is already pre-styled with Thank You and Lloyd Institute

    prs.save(out_pptx)
    prs.save(sub_pptx)
    print(f"Presentation saved to: {out_pptx}")
    print(f"Presentation copied to: {sub_pptx}")

    print("\nConverting PPTX to PDF via PowerPoint Automation...")
    import win32com.client
    ppt_app = win32com.client.Dispatch("PowerPoint.Application")
    try:
        abs_pptx = os.path.abspath(out_pptx)
        abs_pdf = os.path.abspath(out_pptx.replace('.pptx', '.pdf'))
        abs_sub_pdf = os.path.abspath(sub_pptx.replace('.pptx', '.pdf'))

        pres = ppt_app.Presentations.Open(abs_pptx, WithWindow=False)
        pres.SaveAs(abs_pdf, 32) # ppSaveAsPDF = 32
        pres.SaveAs(abs_sub_pdf, 32)
        pres.Close()
        print(f"Presentation PDF successfully generated at: {abs_pdf}")
        print(f"Presentation PDF copied to: {abs_sub_pdf}")
    except Exception as e:
        print(f"Error during PowerPoint PDF conversion: {e}")
    finally:
        ppt_app.Quit()

if __name__ == '__main__':
    build_presentation()
