from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from build_report.helpers import (
    add_heading_1, add_heading_2, add_heading_3, add_body_p, add_bullet_p,
    add_code_block, add_table_custom
)

def add_references_and_appendix(doc):
    # REFERENCES
    add_heading_1(doc, "REFERENCES")
    add_body_p(
        doc,
        "All citations follow standard IEEE referencing guidelines and represent authoritative research in Natural Language "
        "Processing, computational linguistics, machine learning, and digital misinformation forensics:",
        space_after=12
    )

    refs = [
        "[1] B. Xie, X. Ma, and X. Shan, 'Multiknowledge and LLM-Inspired Heterogeneous Graph Neural Network for Fake News Detection,' IEEE Transactions on Computational Social Systems, vol. 12, no. 2, pp. 682–694, 2025.",
        "[2] B. Cao, Q. Wu, J. Cao, B. Liu, and J. Gui, 'External Reliable Information-enhanced Multimodal Contrastive Learning for Fake News Detection,' in Proceedings of the AAAI Conference on Artificial Intelligence, vol. 39, pp. 31–39, 2025.",
        "[3] L. Xiao, Q. Zhang, C. Shi, S. Wang, U. Naseem, and L. Hu, 'MSynFD: Multi-Hop Syntax-Aware Fake News Detection,' in Proceedings of the ACM Web Conference (WWW '24), pp. 4112–4123, 2024.",
        "[4] Y. Sun, Q. Huang, A. K. H. Tung, and J. Yu, 'PRISM: A Framework for Producing Interpretable Political Bias Embeddings with Political-Aware Cross-Encoder,' in Proceedings of the Association for Computational Linguistics (ACL 2025), pp. 1520–1534, 2025.",
        "[5] X. Zheng, Z. Zeng, H. Wang, Y. Bai, and M. Luo, 'From Predictions to Analyses: Rationale-Augmented Fake News Detection with Large Vision-Language Models,' in Proceedings of the ACM Web Conference (WWW '25), pp. 2410–2421, 2025.",
        "[6] S. Hu, J. Hu, and H. Zhang, 'Synergizing LLMs with Global Label Propagation for Multimodal Fake News Detection (GLPN-LLM),' in Findings of the Association for Computational Linguistics (ACL 2025), pp. 3120–3133, 2025.",
        "[7] Y. Lei and R. Huang, 'Boosting Logical Fallacy Reasoning in LLMs via Logical Structure Tree,' in Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP 2024), pp. 1820–1835, 2024.",
        "[8] M.-H. Yeh, R. Wan, and T.-H. K. Huang, 'CoCoLoFa: A Dataset of News Comments with Common Logical Fallacies Written by LLM-Assisted Crowds,' in Proceedings of EMNLP 2024, pp. 4501–4514, 2024.",
        "[9] R. Rönnback, C. Emmery, and H. Brighton, 'Automatic Large-Scale Political Bias Detection of News Outlets,' PLOS ONE, vol. 20, no. 5, p. e0321418, 2025.",
        "[10] X. Wang, E. Cabrio, and S. Villata, 'When Automated Fact-Checking Meets Argumentation: Unveiling Fake News Through Argumentative Evidence,' Argument & Computation, vol. 16, no. 3, pp. 210–235, 2025.",
        "[11] H. Ahmed, I. Traore, and S. Saad, 'Detecting opinion spams and fake news using text classification,' Security and Privacy, vol. 1, no. 1, p. e9, 2018.",
        "[12] V. L. Rubin, Y. Chen, and N. J. Conroy, 'Deception detection for news: Three types of fakes,' Proceedings of the Association for Information Science and Technology, vol. 52, no. 1, pp. 1–4, 2015.",
        "[13] K. Shu, A. Sliva, S. Wang, J. Tang, and H. Liu, 'Fake news detection on social media: A data mining perspective,' ACM SIGKDD Explorations Newsletter, vol. 19, no. 1, pp. 22–36, 2017.",
        "[14] X. Zhou and R. Zafarani, 'A survey of fake news: Fundamental theories, detection methods, and opportunities,' ACM Computing Surveys (CSUR), vol. 53, no. 5, pp. 1–40, 2020.",
        "[15] J. Devlin, M. W. Chang, K. Lee, and K. Toutanova, 'BERT: Pre-training of deep bidirectional transformers for language understanding,' arXiv preprint arXiv:1810.04805, 2018.",
        "[16] Y. Liu, M. Ott, N. Goyal, J. Du, M. Joshi, D. Chen, O. Levy, M. Lewis, L. Zettlemoyer, and V. Stoyanov, 'RoBERTa: A robustly optimized BERT pretraining approach,' arXiv preprint arXiv:1907.11692, 2019.",
        "[17] P. He, X. Liu, J. Gao, and W. Chen, 'DeBERTa: Decoding-enhanced BERT with disentangled attention,' in International Conference on Learning Representations (ICLR), 2021.",
        "[18] T. Chen and C. Guestrin, 'XGBoost: A scalable tree boosting system,' in Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, pp. 785–794, 2016.",
        "[19] L. Breiman, 'Random Forests,' Machine Learning, vol. 45, no. 1, pp. 5–32, 2001.",
        "[20] D. H. Wolpert, 'Stacked generalization,' Neural Networks, vol. 5, no. 2, pp. 241–259, 1992.",
        "[21] F. Pedregosa et al., 'Scikit-learn: Machine learning in Python,' Journal of Machine Learning Research, vol. 12, pp. 2825–2830, 2011.",
        "[22] S. Bird, E. Klein, and E. Loper, Natural Language Processing with Python: Analyzing Text with the Natural Language Toolkit, O'Reilly Media, 2009.",
        "[23] UNESCO, 'Global report on information integrity and digital platforms,' United Nations Educational, Scientific and Cultural Organization, Paris, Tech. Rep., 2025.",
        "[24] World Economic Forum, 'The Global Risks Report 2024–2025,' Insight Report, 19th Edition, Geneva, Switzerland, 2024.",
        "[25] J. P. Kincaid, R. P. Fishburne, R. L. Rogers, and B. S. Chissom, 'Derivation of new readability formulas for Navy enlisted personnel,' Research Branch Report 8-75, Chief of Naval Technical Training, Naval Air Station Memphis, 1975."
    ]

    for ref in refs:
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.line_spacing = 1.15
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        r = p.add_run(ref)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(9.5)

    # APPENDIX
    doc.add_page_break()
    add_heading_1(doc, "APPENDIX")

    add_heading_2(doc, "Appendix A: Mathematical Derivations and Epistemic Formulations")
    add_body_p(
        doc,
        "A.1 Derivation of Simpson's Diversity Index (D_simpson): In ecological statistics, Simpson's Index quantifies the "
        "probability that two individuals randomly chosen from a finite sample belong to different categories. Translating this "
        "to natural language text, let N be the total number of words in a document and n_i be the occurrence frequency of the "
        "i-th vocabulary token. The probability of randomly drawing two identical words with replacement is:"
    )
    add_body_p(
        doc,
        "    lambda = sum_{i=1}^V [ n_i * (n_i - 1) ] / [ N * (N - 1) ]",
        bold_prefix="Formulation: "
    )
    add_body_p(
        doc,
        "The Gini-Simpson diversity measure D_simpson = 1 - lambda bounded in [0, 1]. In authentic investigative journalism with "
        "rich vocabulary, lambda is small and D_simpson approaches 1.0. In formulaic or synthesized propaganda with repetitive "
        "cues, lambda increases and D_simpson degrades noticeably."
    )
    add_body_p(
        doc,
        "A.2 Stacking Ensemble Binary Cross-Entropy Optimization: Let z_i in R^4 represent the blended base-learner probability "
        "predictions for the i-th training sample. The regularized meta-learner solves the convex optimization problem:"
    )
    add_body_p(
        doc,
        "    L(w) = (1 / 2) * ||w||_2^2 + C * sum_{i=1}^M log( 1 + exp( -y_i * ( w^T z_i + b ) ) )",
        bold_prefix="Optimization Objective: "
    )
    add_body_p(
        doc,
        "Solved using L-BFGS quasi-Newton gradient updates, ensuring optimal probability calibration and preventing over-confidence."
    )

    add_heading_2(doc, "Appendix B: Complete Feature Vector Schema (5,028 Dimensions)")
    add_body_p(
        doc,
        "Table B.1 details the exact schema, normalization transform, and dimensional mapping of the fused feature vector X_fused:"
    )

    f_schema = [
        ["0 – 3", "TTR, RTTR, CTTR, BiTTR", "StandardScaler", "Lexical richness and vocabulary variation."],
        ["4 – 5", "Hapax Legomena & Dis Legomena Ratios", "StandardScaler", "Rare word usage and vocabulary depth."],
        ["6 – 7", "Simpson's Diversity & Shannon Lexical Entropy", "StandardScaler", "Vocabulary concentration and information density."],
        ["8 – 12", "Flesch Reading Ease, FKGL, GFI, ARI, CLI", "StandardScaler", "Cognitive fluency, syllable ratios, grade level."],
        ["13 – 17", "Punctuation Densities & Punctuation Entropy", "StandardScaler", "Exclamation, question, quotation marks, commas."],
        ["18 – 19", "Subjectivity Index & Sentiment Polarity", "StandardScaler", "Authorial subjectivity and emotional tone."],
        ["20 – 21", "Emotional Hyperbole (EHF) & Hedging (HUR)", "StandardScaler", "Sensational modifier density and speculative hedging."],
        ["22 – 23", "Polarity Delta & Affective Polarization Density", "StandardScaler", "Headline-body divergence and sentence polarity variance."],
        ["24 – 25", "Composite Author Bias Score (ABS) & Fallacy Index (FSI)", "StandardScaler", "Aggregated 0–100 author bias and rhetorical fallacy penalty."],
        ["26 – 27", "AllSides 2D Coordinates (Bias_x, Fact_y)", "StandardScaler", "Directional ideological spectrum and epistemic factuality."],
        ["28 – 5027", "Sublinear TF-IDF N-grams (1–2 grams)", "Sublinear TF + L2 Norm", "High-dimensional sparse lexical and topical vocabulary."]
    ]
    add_table_custom(
        doc,
        headers=["Feature Indices", "Feature Category & Extracted Metrics", "Scaling Method", "Epistemic Significance"],
        rows_data=f_schema,
        caption_text="Exhaustive Dimensional Breakdown of the 5,028 Fused Feature Vector.",
        table_num="Table B.1",
        col_widths=[1.2, 2.2, 1.2, 2.17]
    )

    add_heading_2(doc, "Appendix C: Curated Institutional Consensus Knowledge Matrices")
    add_body_p(
        doc,
        "The knowledge grounding database stores canonical consensus statements from global authorities:"
    )
    add_bullet_p(
        doc,
        "Keywords: ['cancer cure', 'miracle cure', 'destroy cancer overnight']. Consensus: Cancer comprises over 100 distinct pathologies requiring targeted clinical regimens. There is no universal single-ingredient cure. Authority: WHO & National Cancer Institute (https://www.who.int/news-room/fact-sheets/detail/cancer).",
        bold_prefix="Oncology Matrix (WHO / NCI): "
    )
    add_bullet_p(
        doc,
        "Keywords: ['vaccine microchip', 'dna alteration', 'poisoned vaccines']. Consensus: Approved vaccines undergo multi-phase double-blind clinical trials verifying safety. Vaccines do not alter DNA and contain no tracking microchips. Authority: WHO & CDC (https://www.who.int/initiatives/act-accelerator/covax).",
        bold_prefix="Immunology Matrix (WHO / CDC): "
    )
    add_bullet_p(
        doc,
        "Keywords: ['asteroid will destroy earth', 'nasa hiding apocalypse']. Consensus: NASA CNEOS tracks all Near-Earth Objects. There are no known significant asteroid impact risks for the next 100+ years. Authority: NASA CNEOS (https://cneos.jpl.nasa.gov/).",
        bold_prefix="Astrophysics Matrix (NASA CNEOS): "
    )
    add_bullet_p(
        doc,
        "Keywords: ['climate change is hoax', 'global cooling', 'ice age coming']. Consensus: Over 99% of actively publishing climate scientists agree human industrial emissions are warming the climate system. Authority: IPCC AR6 (https://www.ipcc.ch/report/ar6/wg1/).",
        bold_prefix="Climatology Matrix (IPCC AR6): "
    )

    add_heading_2(doc, "Appendix D: System Configuration and Package Manifest")
    add_body_p(
        doc,
        "The system configuration file (`config.py`) specifies application ports, thresholds, and hyperparameters:"
    )

    code_cfg = """
# System Configuration Parameters (config.py)
SERVER_HOST = "0.0.0.0"
SERVER_PORT = 5001
DEBUG_MODE = False
SECRET_KEY = "audit-epistemic-secret-key-2026"

# Model & Feature Thresholds
MAX_TFIDF_FEATURES = 5000
NGRAM_RANGE = (1, 2)
SUBLINEAR_TF = True
DECISION_THRESHOLD = 0.50

# Fallacy Severity Thresholds
FSI_LOW_THRESHOLD = 20.0
FSI_HIGH_THRESHOLD = 50.0

# Author Bias Thresholds
ABS_OBJECTIVE_THRESHOLD = 25.0
ABS_SENSATIONAL_THRESHOLD = 60.0

# Networking & Ingestion
SOCKET_TIMEOUT = 5.0
MAX_CONTENT_LENGTH = 10 * 1024 * 1024  # 10 MB
RATE_LIMIT_PER_MINUTE = 30
DEFAULT_RSS_FEED = "http://feeds.bbci.co.uk/news/world/rss.xml"
"""
    add_code_block(doc, code_cfg, title="System Configuration Manifest (config.py)")

    add_heading_2(doc, "Appendix E: Interactive Web Telemetry User Interface Guide")
    add_body_p(
        doc,
        "The Evidence and Framing Auditor provides an intuitive web interface accessible on Port 5001. The interface comprises "
        "three primary visual components:"
    )
    add_bullet_p(
        doc,
        "Allows users to type or paste news text, submit any live HTTP/HTTPS article URL for automatic DOM scraping, "
        "or select one-click live RSS feed articles from BBC World News.",
        bold_prefix="1. Ingestion Control Panel: "
    )
    add_bullet_p(
        doc,
        "Visualizes the article's ideological stance on an interactive continuous 2D grid (X-axis: Left to Right; "
        "Y-axis: Factuality 0.0 to 1.0) alongside circular SVG dials for Composite Author Bias Score (ABS) and Fallacy Severity Index (FSI).",
        bold_prefix="2. AllSides 2D Stance Canvas & Bias Gauges: "
    )
    add_bullet_p(
        doc,
        "Renders the full article with individual sentences color-coded in green (objective / verified), "
        "amber (unsubstantiated hedging / mild bias), or red (rhetorical fallacy / institutional factual contradiction), accompanied "
        "by expandable cards detailing the exact matched linguistic cue and official institutional refutation URL.",
        bold_prefix="3. Sentence-Level Explainability Inspector: "
    )
