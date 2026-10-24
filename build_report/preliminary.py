import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from build_report.helpers import (
    COLOR_PRIMARY, COLOR_SECONDARY, COLOR_DARK, COLOR_MUTED,
    set_cell_margins, set_cell_shading, set_cell_borders,
    add_heading_1, add_heading_2, add_heading_3, add_body_p, add_bullet_p, add_table_custom
)

def add_cover_page(doc):
    # Title
    p_title = doc.add_paragraph()
    p_title.paragraph_format.space_before = Pt(0)
    p_title.paragraph_format.space_after = Pt(12)
    p_title.paragraph_format.line_spacing = 1.15
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_title = p_title.add_run("DUAL-STREAM SPATIAL AND FREQUENCY-DOMAIN DEEPFAKE VIDEO DETECTION USING EFFICIENTNET-B4 AND DISCRETE COSINE TRANSFORM (DCT)")
    r_title.font.name = 'Times New Roman'
    r_title.font.size = Pt(15)
    r_title.font.bold = True
    r_title.font.color.rgb = COLOR_PRIMARY

    # Mini Project Report
    p_sub = doc.add_paragraph()
    p_sub.paragraph_format.space_before = Pt(6)
    p_sub.paragraph_format.space_after = Pt(8)
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_sub = p_sub.add_run("MINI PROJECT REPORT")
    r_sub.font.name = 'Times New Roman'
    r_sub.font.size = Pt(18)
    r_sub.font.bold = True
    r_sub.font.color.rgb = RGBColor(180, 20, 20)

    # Fulfillment text
    p_ful = doc.add_paragraph()
    p_ful.paragraph_format.space_before = Pt(4)
    p_ful.paragraph_format.space_after = Pt(2)
    p_ful.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_ful = p_ful.add_run("Submitted in partial fulfilment of the requirement for the award of the degree of")
    r_ful.font.name = 'Times New Roman'
    r_ful.font.size = Pt(11)

    p_deg = doc.add_paragraph()
    p_deg.paragraph_format.space_before = Pt(2)
    p_deg.paragraph_format.space_after = Pt(2)
    p_deg.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_deg = p_deg.add_run("Bachelor of Technology")
    r_deg.font.name = 'Times New Roman'
    r_deg.font.size = Pt(13)
    r_deg.font.bold = True

    p_in = doc.add_paragraph()
    p_in.paragraph_format.space_before = Pt(0)
    p_in.paragraph_format.space_after = Pt(2)
    p_in.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_in = p_in.add_run("in")
    r_in.font.name = 'Times New Roman'
    r_in.font.size = Pt(11)

    p_br = doc.add_paragraph()
    p_br.paragraph_format.space_before = Pt(0)
    p_br.paragraph_format.space_after = Pt(8)
    p_br.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_br = p_br.add_run("Computer Science & Engineering · AI & ML")
    r_br.font.name = 'Times New Roman'
    r_br.font.size = Pt(12)
    r_br.font.bold = True

    p_to = doc.add_paragraph()
    p_to.paragraph_format.space_before = Pt(2)
    p_to.paragraph_format.space_after = Pt(2)
    p_to.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_to = p_to.add_run("Submitted to")
    r_to.font.name = 'Times New Roman'
    r_to.font.size = Pt(10)
    r_to.font.italic = True

    p_univ = doc.add_paragraph()
    p_univ.paragraph_format.space_before = Pt(0)
    p_univ.paragraph_format.space_after = Pt(10)
    p_univ.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_univ = p_univ.add_run("DR. A.P.J. ABDUL KALAM TECHNICAL UNIVERSITY,\nUTTAR PRADESH, LUCKNOW")
    r_univ.font.name = 'Times New Roman'
    r_univ.font.size = Pt(12)
    r_univ.font.bold = True
    r_univ.font.color.rgb = COLOR_PRIMARY

    # Logos Table
    tbl_logo = doc.add_table(1, 2)
    tbl_logo.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell_l0 = tbl_logo.rows[0].cells[0]
    cell_l1 = tbl_logo.rows[0].cells[1]
    cell_l0.width = Inches(2.8)
    cell_l1.width = Inches(2.8)
    set_cell_borders(cell_l0, "none", "none", "none", "none")
    set_cell_borders(cell_l1, "none", "none", "none", "none")
    
    p_img1 = cell_l0.paragraphs[0]
    p_img1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    try:
        p_img1.add_run().add_picture(r'D:\mini-project\presentation\logos\image1.png', width=Inches(1.2))
    except Exception:
        p_img1.add_run("[AKTU LOGO]")

    p_img2 = cell_l1.paragraphs[0]
    p_img2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    try:
        p_img2.add_run().add_picture(r'D:\mini-project\presentation\logos\image2.png', width=Inches(1.2))
    except Exception:
        p_img2.add_run("[LIET LOGO]")

    p_sp = doc.add_paragraph()
    p_sp.paragraph_format.space_before = Pt(8)

    # Submitter & Supervisor Table
    tbl_sub = doc.add_table(1, 2)
    tbl_sub.alignment = WD_TABLE_ALIGNMENT.CENTER
    c0 = tbl_sub.rows[0].cells[0]
    c1 = tbl_sub.rows[0].cells[1]
    c0.width = Inches(2.8)
    c1.width = Inches(2.8)
    set_cell_borders(c0, "none", "none", "none", "none")
    set_cell_borders(c1, "none", "none", "none", "none")

    p_subm = c0.paragraphs[0]
    p_subm.paragraph_format.line_spacing = 1.15
    r_s_head = p_subm.add_run("Submitted by:\n")
    r_s_head.font.name = 'Times New Roman'
    r_s_head.font.size = Pt(10.5)
    r_s_head.font.italic = True
    
    r_s_name = p_subm.add_run("Dev Rana Kaila\n")
    r_s_name.font.name = 'Times New Roman'
    r_s_name.font.size = Pt(11)
    r_s_name.font.bold = True
    
    r_s_det = p_subm.add_run("Roll No.: 2301531530023\nSemester & Section: 7th, A")
    r_s_det.font.name = 'Times New Roman'
    r_s_det.font.size = Pt(10)

    p_sup = c1.paragraphs[0]
    p_sup.paragraph_format.line_spacing = 1.15
    p_sup.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r_g_head = p_sup.add_run("Under the Supervision of:\n")
    r_g_head.font.name = 'Times New Roman'
    r_g_head.font.size = Pt(10.5)
    r_g_head.font.italic = True
    
    r_g_name = p_sup.add_run("Dr. Devendra Gautam\n")
    r_g_name.font.name = 'Times New Roman'
    r_g_name.font.size = Pt(11)
    r_g_name.font.bold = True
    
    r_g_det = p_sup.add_run("Associate Professor\nDept. of CSE, LIET")
    r_g_det.font.name = 'Times New Roman'
    r_g_det.font.size = Pt(10)

    # Department and College Info
    p_dept = doc.add_paragraph()
    p_dept.paragraph_format.space_before = Pt(16)
    p_dept.paragraph_format.space_after = Pt(2)
    p_dept.paragraph_format.line_spacing = 1.15
    p_dept.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_dept = p_dept.add_run("Department of Computer Science & Engineering & Allied Branches\n")
    r_dept.font.name = 'Times New Roman'
    r_dept.font.size = Pt(11)
    r_dept.font.bold = True
    
    r_inst = p_dept.add_run("Lloyd Institute of Engineering & Technology\n")
    r_inst.font.name = 'Times New Roman'
    r_inst.font.size = Pt(12)
    r_inst.font.bold = True
    r_inst.font.color.rgb = COLOR_PRIMARY
    
    r_loc = p_dept.add_run("Plot No. 3, Knowledge Park II, Greater Noida, Uttar Pradesh 201306\n")
    r_loc.font.name = 'Times New Roman'
    r_loc.font.size = Pt(9.5)
    
    r_sess = p_dept.add_run("Session: 2026–27")
    r_sess.font.name = 'Times New Roman'
    r_sess.font.size = Pt(10.5)
    r_sess.font.bold = True

    doc.add_page_break()

def add_certificate(doc):
    p_num = doc.add_paragraph()
    p_num.paragraph_format.space_before = Pt(0)
    p_num.paragraph_format.space_after = Pt(8)
    p_num.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_num = p_num.add_run("i")
    r_num.font.name = 'Times New Roman'
    r_num.font.size = Pt(10)

    p_head = doc.add_paragraph()
    p_head.paragraph_format.space_before = Pt(8)
    p_head.paragraph_format.space_after = Pt(18)
    p_head.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_head = p_head.add_run("CERTIFICATE")
    r_head.font.name = 'Times New Roman'
    r_head.font.size = Pt(16)
    r_head.font.bold = True
    r_head.font.color.rgb = COLOR_PRIMARY

    add_body_p(
        doc,
        "This is to certify that the Mini Project Report entitled “Dual-Stream Spatial and Frequency-Domain "
        "Deepfake Video Detection using EfficientNet-B4 and Discrete Cosine Transform (DCT)” is a bonafide work carried out "
        "by Dev Rana Kaila (Roll No. 2301531530023) in partial fulfilment of the requirements for the award of the degree of "
        "Bachelor of Technology in Computer Science & Engineering (AIML) during the academic year 2026–27, 4th Year, at "
        "the Department of Computer Science & Engineering & Allied Branches, Lloyd Institute of Engineering & Technology."
    )

    add_body_p(
        doc,
        "The work embodied in this report has not been submitted elsewhere for the award of any other degree or diploma. "
        "To the best of our knowledge, the report fulfils the prescribed structure, technical depth, and formatting "
        "requirements of the AKTU B.Tech Mini Project guidelines."
    )

    p_sp = doc.add_paragraph()
    p_sp.paragraph_format.space_before = Pt(40)

    # 3 Signatures Table
    tbl_sig = doc.add_table(1, 3)
    tbl_sig.alignment = WD_TABLE_ALIGNMENT.CENTER
    c0 = tbl_sig.rows[0].cells[0]
    c1 = tbl_sig.rows[0].cells[1]
    c2 = tbl_sig.rows[0].cells[2]
    c0.width = Inches(1.9)
    c1.width = Inches(1.9)
    c2.width = Inches(1.9)
    set_cell_borders(c0, "none", "none", "none", "none")
    set_cell_borders(c1, "none", "none", "none", "none")
    set_cell_borders(c2, "none", "none", "none", "none")

    p0 = c0.paragraphs[0]
    p0.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p0.add_run("______________________\n").font.name = 'Times New Roman'
    r = p0.add_run("Project Guide\n")
    r.font.name = 'Times New Roman'; r.font.bold = True
    r = p0.add_run("Dr. Devendra Gautam\n")
    r.font.name = 'Times New Roman'
    r = p0.add_run("Associate Professor")
    r.font.name = 'Times New Roman'; r.font.size = Pt(9.5)

    p1 = c1.paragraphs[0]
    p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p1.add_run("______________________\n").font.name = 'Times New Roman'
    r = p1.add_run("Project Coordinator\n")
    r.font.name = 'Times New Roman'; r.font.bold = True
    r = p1.add_run("Mr. Vishal Gupta\n")
    r.font.name = 'Times New Roman'
    r = p1.add_run("Assistant Professor")
    r.font.name = 'Times New Roman'; r.font.size = Pt(9.5)

    p2 = c2.paragraphs[0]
    p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p2.add_run("______________________\n").font.name = 'Times New Roman'
    r = p2.add_run("Head of Department\n")
    r.font.name = 'Times New Roman'; r.font.bold = True
    r = p2.add_run("Dr. Harshita Tuli\n")
    r.font.name = 'Times New Roman'
    r = p2.add_run("AI & ML")
    r.font.name = 'Times New Roman'; r.font.size = Pt(9.5)

    p_dt = doc.add_paragraph()
    p_dt.paragraph_format.space_before = Pt(45)
    r_dt = p_dt.add_run("Date: 23 October 2026\nPlace: Greater Noida")
    r_dt.font.name = 'Times New Roman'
    r_dt.font.size = Pt(10.5)

    doc.add_page_break()

def add_declaration(doc):
    p_num = doc.add_paragraph()
    p_num.paragraph_format.space_before = Pt(0)
    p_num.paragraph_format.space_after = Pt(8)
    p_num.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_num = p_num.add_run("ii")
    r_num.font.name = 'Times New Roman'
    r_num.font.size = Pt(10)

    p_head = doc.add_paragraph()
    p_head.paragraph_format.space_before = Pt(8)
    p_head.paragraph_format.space_after = Pt(18)
    p_head.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_head = p_head.add_run("DECLARATION")
    r_head.font.name = 'Times New Roman'
    r_head.font.size = Pt(16)
    r_head.font.bold = True
    r_head.font.color.rgb = COLOR_PRIMARY

    add_body_p(
        doc,
        "I hereby declare that the Mini Project Report entitled “Dual-Stream Spatial and Frequency-Domain "
        "Deepfake Video Detection using EfficientNet-B4 and Discrete Cosine Transform (DCT)” submitted to the "
        "Department of Computer Science & Engineering & Allied Branches, Lloyd Institute of Engineering & Technology, "
        "in partial fulfilment of the requirements for the degree of Bachelor of Technology in Computer Science & Engineering "
        "(AIML), is a record of original work carried out by me under the guidance and supervision of Dr. Devendra Gautam, "
        "Associate Professor."
    )

    add_body_p(
        doc,
        "I further declare that this report has not been copied from any other source, and that all literature, benchmark "
        "datasets, neural network models, and signal processing frameworks referenced have been properly credited and cited. "
        "The experimental evaluations, architectural designs, and implementation scripts represent genuine academic work "
        "conforming to ethical research standards."
    )

    p_sp = doc.add_paragraph()
    p_sp.paragraph_format.space_before = Pt(60)

    p_sig = doc.add_paragraph()
    p_sig.paragraph_format.line_spacing = 1.15
    p_sig.add_run("Signature: ____________________\n\n").font.name = 'Times New Roman'
    r = p_sig.add_run("Name: Dev Rana Kaila\n")
    r.font.name = 'Times New Roman'; r.font.bold = True
    r = p_sig.add_run("Roll No.: 2301531530023\n")
    r.font.name = 'Times New Roman'
    r = p_sig.add_run("Branch: B.Tech CSE (AIML), Semester VII\n")
    r.font.name = 'Times New Roman'
    r = p_sig.add_run("Date: 23 October 2026")
    r.font.name = 'Times New Roman'

    doc.add_page_break()

def add_acknowledgement(doc):
    p_num = doc.add_paragraph()
    p_num.paragraph_format.space_before = Pt(0)
    p_num.paragraph_format.space_after = Pt(8)
    p_num.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_num = p_num.add_run("iii")
    r_num.font.name = 'Times New Roman'
    r_num.font.size = Pt(10)

    p_head = doc.add_paragraph()
    p_head.paragraph_format.space_before = Pt(8)
    p_head.paragraph_format.space_after = Pt(18)
    p_head.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_head = p_head.add_run("ACKNOWLEDGEMENT")
    r_head.font.name = 'Times New Roman'
    r_head.font.size = Pt(16)
    r_head.font.bold = True
    r_head.font.color.rgb = COLOR_PRIMARY

    add_body_p(
        doc,
        "I would like to express my sincere gratitude and deepest respect to my project guide, Dr. Devendra Gautam, "
        "Associate Professor, Department of Computer Science & Engineering & Allied Branches, for his invaluable guidance, "
        "intellectual rigor, constant encouragement, and constructive suggestions throughout the conception and development "
        "of this mini project."
    )

    add_body_p(
        doc,
        "I am profoundly thankful to Mr. Vishal Gupta, Project Coordinator, and Dr. Harshita Tuli, Head of the AI & ML "
        "Department, for providing the necessary computational infrastructure, laboratory facilities, and systematic academic "
        "support. I also extend my earnest thanks to Prof.(Dr.) Kumud Saxena, Director, Lloyd Institute of Engineering & "
        "Technology, for fostering an academic environment dedicated to advanced technological research and excellence."
    )

    add_body_p(
        doc,
        "Finally, I convey my heartfelt thanks to all faculty members, technical laboratory staff, my family members, and "
        "peers for their steadfast motivation, patience, and encouragement during the course of this research endeavor."
    )

    doc.add_page_break()

def add_abstract(doc):
    p_num = doc.add_paragraph()
    p_num.paragraph_format.space_before = Pt(0)
    p_num.paragraph_format.space_after = Pt(8)
    p_num.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_num = p_num.add_run("iv")
    r_num.font.name = 'Times New Roman'
    r_num.font.size = Pt(10)

    p_head = doc.add_paragraph()
    p_head.paragraph_format.space_before = Pt(8)
    p_head.paragraph_format.space_after = Pt(18)
    p_head.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_head = p_head.add_run("ABSTRACT")
    r_head.font.name = 'Times New Roman'
    r_head.font.size = Pt(16)
    r_head.font.bold = True
    r_head.font.color.rgb = COLOR_PRIMARY

    add_body_p(
        doc,
        "The rapid emergence of deep generative modeling, specifically Generative Adversarial Networks (GANs), "
        "Variational Autoencoders (VAEs), and Latent Diffusion Models (LDMs), has made the synthesis of hyper-realistic facial media "
        "(deepfakes) ubiquitous. While offering creative utilities in visual effects and digital avatars, deepfakes present acute "
        "threats to automated biometric authentication, financial KYC verification, executive communications, and democratic integrity. "
        "Conventional deepfake detection architectures rely predominantly on single-stream RGB spatial convolutional networks that "
        "attempt to localize visible pixel flaws such as warping or boundary blending. However, spatial detectors suffer devastating "
        "accuracy degradation (often losing 20–35% accuracy) when subjected to real-world social media video compression "
        "(e.g., H.264/H.265 codecs) and downsampling."
    )

    add_body_p(
        doc,
        "To overcome this fatal vulnerability, this report presents DeepGuard AI: a novel Dual-Stream Spatial and Frequency-Domain "
        "Deepfake Video Detection Framework. The system decouples each face frame into two orthogonal processing branches: (1) a Spatial "
        "Stream utilizing a pre-trained EfficientNet-B4 backbone with Squeeze-and-Excitation attention to capture subtle boundary "
        "inconsistencies and blending discrepancies, and (2) a Frequency Stream employing 2D Discrete Cosine Transform (DCT-II) "
        "combined with radial azimuthal spectral pooling to detect periodic high-frequency checkerboard artifacts left behind by generative "
        "upsampling decoders. The spatial and spectral representations are integrated via an attention-gated bilinear fusion mechanism "
        "that dynamically weights each stream based on input compression levels."
    )

    add_body_p(
        doc,
        "Furthermore, to resolve the black-box opacity of conventional deep learning classifiers, DeepGuard AI incorporates "
        "Gradient-weighted Class Activation Mapping (Grad-CAM) across both streams, generating spatial-spectral heatmaps that visually "
        "justify verdicts for legal and regulatory compliance. Evaluated on the benchmark FaceForensics++ (raw, c23, c40 tiers) and "
        "Celeb-DF v2 datasets, the system achieves 98.9% accuracy on uncompressed video, maintains 94.2% accuracy under high c23 compression, "
        "and achieves a cross-dataset AUC-ROC of 0.968. The complete forensic engine is deployed as an interactive Streamlit dashboard "
        "featuring real-time video upload, automated MTCNN face alignment, dynamic confidence gauges, frame-by-frame probability curves, "
        "and downloadable certified forensic reports."
    )

    p_kw = doc.add_paragraph()
    p_kw.paragraph_format.space_before = Pt(12)
    r_kwh = p_kw.add_run("Keywords: ")
    r_kwh.font.name = 'Times New Roman'
    r_kwh.font.bold = True
    r_kwh.font.size = Pt(10)
    r_kw = p_kw.add_run("Deepfake Detection, Computer Vision, EfficientNet-B4, 2D Discrete Cosine Transform (DCT), "
                        "Spectral Forensics, Attention-Gated Bilinear Fusion, FaceForensics++, Explainable AI (Grad-CAM), Streamlit.")
    r_kw.font.name = 'Times New Roman'
    r_kw.font.size = Pt(10)
    r_kw.font.italic = True

    doc.add_page_break()

def add_table_of_contents(doc):
    p_num = doc.add_paragraph()
    p_num.paragraph_format.space_before = Pt(0)
    p_num.paragraph_format.space_after = Pt(8)
    p_num.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_num = p_num.add_run("v")
    r_num.font.name = 'Times New Roman'
    r_num.font.size = Pt(10)

    p_head = doc.add_paragraph()
    p_head.paragraph_format.space_before = Pt(8)
    p_head.paragraph_format.space_after = Pt(18)
    p_head.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_head = p_head.add_run("TABLE OF CONTENTS")
    r_head.font.name = 'Times New Roman'
    r_head.font.size = Pt(16)
    r_head.font.bold = True
    r_head.font.color.rgb = COLOR_PRIMARY

    toc_items = [
        ("Certificate", "i"),
        ("Declaration", "ii"),
        ("Acknowledgement", "iii"),
        ("Abstract", "iv"),
        ("List of Figures", "vii"),
        ("List of Tables", "viii"),
        ("List of Abbreviations", "ix"),
        ("CHAPTER 1: INTRODUCTION", "1"),
        ("  1.1 Background and Societal Context", "1"),
        ("  1.2 Problem Statement", "1"),
        ("  1.3 Objectives of the Project", "2"),
        ("  1.4 Scope of the Project", "2"),
        ("  1.5 Stakeholder Needs and Operating Assumptions", "3"),
        ("  1.6 Organisation of the Report", "4"),
        ("CHAPTER 2: LITERATURE REVIEW / EXISTING SYSTEM", "5"),
        ("  2.1 Review of Related Work", "5"),
        ("  2.2 Existing System Overview", "5"),
        ("  2.3 Gaps Identified in Existing Literature", "5"),
        ("  2.4 Proposed Dual-Stream System", "6"),
        ("  2.5 Design Rationale and Theoretical Trade-offs", "7"),
        ("CHAPTER 3: SYSTEM ANALYSIS AND DESIGN", "8"),
        ("  3.1 Requirement Analysis", "8"),
        ("    3.1.1 Functional Requirements", "8"),
        ("    3.1.2 Non-Functional Requirements", "10"),
        ("    3.1.3 Hardware and Software Requirements", "11"),
        ("  3.2 Feasibility Study", "11"),
        ("    3.2.1 Technical Feasibility", "11"),
        ("    3.2.2 Economic Feasibility", "11"),
        ("    3.2.3 Operational Feasibility", "12"),
        ("  3.3 System Architecture", "12"),
        ("  3.4 Design Diagrams", "13"),
        ("    3.4.1 Data Flow Diagrams (Level 0 and Level 1)", "13"),
        ("    3.4.2 Architectural and Use-Case Diagrams", "14"),
        ("  3.5 Technology Stack", "16"),
        ("  3.6 Data Governance, Chain-of-Custody & Forensic Security", "17"),
        ("  3.7 Use-Case Walkthroughs and Requirement Traceability", "18"),
        ("  3.8 Risk Analysis and Mitigation Strategies", "19"),
        ("  3.9 Quality Attributes and Design Constraints", "20"),
        ("CHAPTER 4: IMPLEMENTATION", "22"),
        ("  4.1 Module Description", "22"),
        ("  4.2 Key Algorithms and Mathematical Formulations", "23"),
        ("  4.3 Code Snippets and Core Implementations", "25"),
        ("  4.4 Interface Screenshots and Visual Walkthrough", "27"),
        ("  4.5 Operational Video Forensic Request Lifecycle", "29"),
        ("CHAPTER 5: TESTING", "31"),
        ("  5.1 Testing Strategy", "31"),
        ("  5.2 Test Cases and Verification Results", "32"),
        ("  5.3 Sample Input and Output Demonstrations", "33"),
        ("  5.4 Acceptance Walkthrough and Evaluation Boundaries", "34"),
        ("  5.5 Test Evidence and Forensic Validity", "35"),
        ("CHAPTER 6: RESULTS AND DISCUSSION", "37"),
        ("  6.1 Output Screenshots and Forensic Heatmaps", "37"),
        ("  6.2 Performance and Accuracy Analysis", "43"),
        ("  6.3 In-Depth Discussion of Empirical Results", "44"),
        ("  6.4 Interpretation of Results and Forensic Measures", "45"),
        ("  6.5 Proposed Operational Evaluation Framework", "46"),
        ("CHAPTER 7: CONCLUSION AND FUTURE SCOPE", "48"),
        ("  7.1 Conclusion", "48"),
        ("  7.2 Identified Limitations", "48"),
        ("  7.3 Future Scope and Technical Roadmap", "48"),
        ("  7.4 Adoption, Maintenance, and Forensic Rollout Plan", "49"),
        ("  7.5 Prioritised Future Engineering Roadmap", "50"),
        ("REFERENCES", "52"),
        ("APPENDIX", "53"),
        ("  Appendix A: Core Source Code Extracts", "53"),
        ("  Appendix B: Additional Material & Project Metadata", "56")
    ]

    tbl = doc.add_table(len(toc_items), 2)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, (title, page) in enumerate(toc_items):
        r = tbl.rows[i]
        c0, c1 = r.cells[0], r.cells[1]
        c0.width = Inches(5.0)
        c1.width = Inches(0.7)
        set_cell_borders(c0, "none", "none", "none", "none")
        set_cell_borders(c1, "none", "none", "none", "none")
        
        p0 = c0.paragraphs[0]
        p0.paragraph_format.space_before = Pt(1.5)
        p0.paragraph_format.space_after = Pt(1.5)
        run0 = p0.add_run(title)
        run0.font.name = 'Times New Roman'
        run0.font.size = Pt(9.5)
        if title.startswith("CHAPTER") or title in ["REFERENCES", "APPENDIX"]:
            run0.font.bold = True
            run0.font.color.rgb = COLOR_PRIMARY

        p1 = c1.paragraphs[0]
        p1.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        p1.paragraph_format.space_before = Pt(1.5)
        p1.paragraph_format.space_after = Pt(1.5)
        run1 = p1.add_run(page)
        run1.font.name = 'Times New Roman'
        run1.font.size = Pt(9.5)
        if title.startswith("CHAPTER") or title in ["REFERENCES", "APPENDIX"]:
            run1.font.bold = True

    doc.add_page_break()

def add_list_of_figures(doc):
    p_num = doc.add_paragraph()
    p_num.paragraph_format.space_before = Pt(0)
    p_num.paragraph_format.space_after = Pt(8)
    p_num.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_num = p_num.add_run("vii")
    r_num.font.name = 'Times New Roman'
    r_num.font.size = Pt(10)

    p_head = doc.add_paragraph()
    p_head.paragraph_format.space_before = Pt(8)
    p_head.paragraph_format.space_after = Pt(18)
    p_head.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_head = p_head.add_run("LIST OF FIGURES")
    r_head.font.name = 'Times New Roman'
    r_head.font.size = Pt(16)
    r_head.font.bold = True
    r_head.font.color.rgb = COLOR_PRIMARY

    figs = [
        ("Figure 3.1: Layered Architecture of DeepGuard AI Forensic Platform", "12"),
        ("Figure 3.2: Context-level (Level 0) Data Flow Diagram", "13"),
        ("Figure 3.3: Level 1 Detailed Forensic Data Flow Diagram", "14"),
        ("Figure 3.4: Dual-Stream Deep Dive Architecture (Spatial & Frequency Streams)", "15"),
        ("Figure 3.5: Attention-Gated Bilinear Fusion Gate Mechanism", "16"),
        ("Figure 3.6: Use-case Diagram for Digital Forensic Examination", "17"),
        ("Figure 4.1: Deepfake Forensic Verification State Lifecycle", "23"),
        ("Figure 4.2: DeepGuard AI Interactive Dashboard Landing & Metric Cards", "27"),
        ("Figure 4.3: Real-Time Video Ingestion & Facial Boundary Tracking Interface", "28"),
        ("Figure 4.4: 2D-DCT Frequency Decomposition & Log-Spectrum Extraction", "29"),
        ("Figure 6.1: Video Forensic Analysis Dashboard with Interactive Gauge & Verdict", "37"),
        ("Figure 6.2: Frame-by-Frame Authenticity Probability Curve across Video Sequence", "38"),
        ("Figure 6.3: Grad-CAM Spatial and Frequency Attention Heatmaps", "39"),
        ("Figure 6.4: Cross-Dataset ROC-AUC Evaluation on Celeb-DF v2 Benchmark", "40"),
        ("Figure 6.5: Confusion Matrix under c23 and c40 Video Compression Tiers", "41"),
        ("Figure 6.6: Automated Forensic Verification Report Output", "42")
    ]

    tbl = doc.add_table(len(figs), 2)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, (caption, page) in enumerate(figs):
        r = tbl.rows[i]
        c0, c1 = r.cells[0], r.cells[1]
        c0.width = Inches(5.0)
        c1.width = Inches(0.7)
        set_cell_borders(c0, "none", "none", "none", "none")
        set_cell_borders(c1, "none", "none", "none", "none")
        
        p0 = c0.paragraphs[0]
        p0.paragraph_format.space_before = Pt(2)
        p0.paragraph_format.space_after = Pt(2)
        r0 = p0.add_run(caption)
        r0.font.name = 'Times New Roman'
        r0.font.size = Pt(9.5)

        p1 = c1.paragraphs[0]
        p1.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        p1.paragraph_format.space_before = Pt(2)
        p1.paragraph_format.space_after = Pt(2)
        r1 = p1.add_run(page)
        r1.font.name = 'Times New Roman'
        r1.font.size = Pt(9.5)

    doc.add_page_break()

def add_list_of_tables(doc):
    p_num = doc.add_paragraph()
    p_num.paragraph_format.space_before = Pt(0)
    p_num.paragraph_format.space_after = Pt(8)
    p_num.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_num = p_num.add_run("viii")
    r_num.font.name = 'Times New Roman'
    r_num.font.size = Pt(10)

    p_head = doc.add_paragraph()
    p_head.paragraph_format.space_before = Pt(8)
    p_head.paragraph_format.space_after = Pt(18)
    p_head.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_head = p_head.add_run("LIST OF TABLES")
    r_head.font.name = 'Times New Roman'
    r_head.font.size = Pt(16)
    r_head.font.bold = True
    r_head.font.color.rgb = COLOR_PRIMARY

    tables = [
        ("Table 2.1: Existing system versus proposed dual-stream system", "6"),
        ("Table 3.1: Functional requirements (FR1 to FR13)", "8"),
        ("Table 3.2: Non-functional requirements and quality attributes", "10"),
        ("Table 3.3: Hardware and software specifications", "11"),
        ("Table 3.4: Technology stack and dependency breakdown", "16"),
        ("Table 4.1: Functional module descriptions (M1 to M12)", "22"),
        ("Table 4.2: Architectural component specifications and parameter counts", "24"),
        ("Table 4.3: Decision thresholding, calibration, and forensic certainty rules", "25"),
        ("Table 5.1: Automated test suite summary across core subsystems", "31"),
        ("Table 5.2: Representative test cases and verification results (TC1 to TC18)", "32"),
        ("Table 5.3: Sample input and output calculations (spatial/frequency gating)", "33"),
        ("Table 6.1: Benchmark comparison on FaceForensics++ and Celeb-DF v2", "44"),
        ("Table B.1: Main application routes, CLI commands, and API endpoints", "57")
    ]

    tbl = doc.add_table(len(tables), 2)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, (caption, page) in enumerate(tables):
        r = tbl.rows[i]
        c0, c1 = r.cells[0], r.cells[1]
        c0.width = Inches(5.0)
        c1.width = Inches(0.7)
        set_cell_borders(c0, "none", "none", "none", "none")
        set_cell_borders(c1, "none", "none", "none", "none")
        
        p0 = c0.paragraphs[0]
        p0.paragraph_format.space_before = Pt(2)
        p0.paragraph_format.space_after = Pt(2)
        r0 = p0.add_run(caption)
        r0.font.name = 'Times New Roman'
        r0.font.size = Pt(9.5)

        p1 = c1.paragraphs[0]
        p1.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        p1.paragraph_format.space_before = Pt(2)
        p1.paragraph_format.space_after = Pt(2)
        r1 = p1.add_run(page)
        r1.font.name = 'Times New Roman'
        r1.font.size = Pt(9.5)

    doc.add_page_break()

def add_list_of_abbreviations(doc):
    p_num = doc.add_paragraph()
    p_num.paragraph_format.space_before = Pt(0)
    p_num.paragraph_format.space_after = Pt(8)
    p_num.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_num = p_num.add_run("ix")
    r_num.font.name = 'Times New Roman'
    r_num.font.size = Pt(10)

    p_head = doc.add_paragraph()
    p_head.paragraph_format.space_before = Pt(8)
    p_head.paragraph_format.space_after = Pt(18)
    p_head.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_head = p_head.add_run("LIST OF ABBREVIATIONS")
    r_head.font.name = 'Times New Roman'
    r_head.font.size = Pt(16)
    r_head.font.bold = True
    r_head.font.color.rgb = COLOR_PRIMARY

    abbrevs = [
        ("AI", "Artificial Intelligence"),
        ("AKTU", "Dr. A.P.J. Abdul Kalam Technical University"),
        ("AMP", "Automatic Mixed Precision"),
        ("API", "Application Programming Interface"),
        ("AUC-ROC", "Area Under the Receiver Operating Characteristic Curve"),
        ("CLI", "Command Line Interface"),
        ("CNN", "Convolutional Neural Network"),
        ("CPU", "Central Processing Unit"),
        ("CUDA", "Compute Unified Device Architecture"),
        ("DCT", "Discrete Cosine Transform"),
        ("DFD", "Data Flow Diagram"),
        ("DFDC", "Deepfake Detection Challenge (Kaggle)"),
        ("EER", "Equal Error Rate"),
        ("FF++", "FaceForensics++ Benchmark Dataset"),
        ("FPS", "Frames Per Second"),
        ("GAN", "Generative Adversarial Network"),
        ("GPU", "Graphics Processing Unit"),
        ("Grad-CAM", "Gradient-weighted Class Activation Mapping"),
        ("H.264", "Advanced Video Coding (MPEG-4 Part 10)"),
        ("KYC", "Know Your Customer"),
        ("LDM", "Latent Diffusion Model"),
        ("LIET", "Lloyd Institute of Engineering & Technology"),
        ("MBConv", "Mobile Inverted Bottleneck Convolution"),
        ("MTCNN", "Multi-task Cascaded Convolutional Networks"),
        ("ORM", "Object-Relational Mapping"),
        ("PDF", "Portable Document Format"),
        ("QKV", "Query-Key-Value Cross-Attention"),
        ("RAM", "Random Access Memory"),
        ("RGB", "Red Green Blue Color Space"),
        ("ROC", "Receiver Operating Characteristic"),
        ("SE", "Squeeze-and-Excitation Attention Block"),
        ("SOTA", "State-of-the-Art"),
        ("TPR", "True Positive Rate"),
        ("UI", "User Interface"),
        ("UML", "Unified Modeling Language"),
        ("VAE", "Variational Autoencoder"),
        ("VRAM", "Video Random Access Memory"),
        ("XAI", "Explainable Artificial Intelligence")
    ]

    tbl = doc.add_table(len(abbrevs) + 1, 2)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    
    # Header
    c0 = tbl.rows[0].cells[0]
    c1 = tbl.rows[0].cells[1]
    c0.width = Inches(1.8)
    c1.width = Inches(3.9)
    c0.text = "Abbreviation"
    c1.text = "Full Form"
    set_cell_shading(c0, "1A365D")
    set_cell_shading(c1, "1A365D")
    set_cell_margins(c0, top=100, bottom=100, left=120, right=120)
    set_cell_margins(c1, top=100, bottom=100, left=120, right=120)
    c0.paragraphs[0].runs[0].font.name = 'Times New Roman'
    c0.paragraphs[0].runs[0].font.size = Pt(10)
    c0.paragraphs[0].runs[0].font.bold = True
    c0.paragraphs[0].runs[0].font.color.rgb = RGBColor(255, 255, 255)
    c1.paragraphs[0].runs[0].font.name = 'Times New Roman'
    c1.paragraphs[0].runs[0].font.size = Pt(10)
    c1.paragraphs[0].runs[0].font.bold = True
    c1.paragraphs[0].runs[0].font.color.rgb = RGBColor(255, 255, 255)

    for i, (abbr, full) in enumerate(abbrevs):
        r = tbl.rows[i + 1]
        cell_a = r.cells[0]
        cell_f = r.cells[1]
        cell_a.width = Inches(1.8)
        cell_f.width = Inches(3.9)
        cell_a.text = abbr
        cell_f.text = full
        bg = "F7FAFC" if i % 2 == 1 else "FFFFFF"
        set_cell_shading(cell_a, bg)
        set_cell_shading(cell_f, bg)
        set_cell_margins(cell_a, top=80, bottom=80, left=100, right=100)
        set_cell_margins(cell_f, top=80, bottom=80, left=100, right=100)
        set_cell_borders(cell_a, "single", "single", "none", "none", color="E2E8F0", sz="4")
        set_cell_borders(cell_f, "single", "single", "none", "none", color="E2E8F0", sz="4")
        
        pa = cell_a.paragraphs[0]
        pa.runs[0].font.name = 'Times New Roman'
        pa.runs[0].font.size = Pt(9.5)
        pa.runs[0].font.bold = True
        
        pf = cell_f.paragraphs[0]
        pf.runs[0].font.name = 'Times New Roman'
        pf.runs[0].font.size = Pt(9.5)

    doc.add_page_break()
