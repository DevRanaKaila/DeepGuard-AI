from build_report.helpers import (
    add_heading_1, add_heading_2, add_heading_3, add_body_p, add_bullet_p
)

def add_chapter_7(doc):
    add_heading_1(doc, "CHAPTER 7: CONCLUSION AND FUTURE SCOPE")

    add_heading_2(doc, "7.1 Summary of Research Accomplishments & Deliverables")
    add_body_p(
        doc,
        "The exponential proliferation of synthetic media, algorithmic computational propaganda, and generative AI disinformation "
        "has underscored the critical necessity for interpretable, epistemically grounded automated fact-checking systems. This mini "
        "project successfully conceptualized, formulated, implemented, and benchmarked the Evidence and Framing Auditor—an end-to-end, "
        "multi-branch Natural Language Processing and Digital Forensics architecture."
    )
    add_body_p(
        doc,
        "The major engineering accomplishments and research contributions delivered by this project include:"
    )
    add_bullet_p(
        doc,
        "Formulated and extracted 18+ mathematical metrics capturing lexical diversity (TTR, RTTR, Simpson's "
        "Diversity, Shannon Lexical Entropy) and cognitive readability (Flesch Reading Ease, Flesch-Kincaid, Gunning Fog).",
        bold_prefix="Multi-Branch Stylometric Engineering: "
    )
    add_bullet_p(
        doc,
        "Derived closed-form equations for Subjectivity Index (S_idx), Emotional Hyperbole Factor (EHF), "
        "Hedging Uncertainty Ratio (HUR), and a Composite Author Bias Score (ABS in [0, 100]), paired with a directional stance "
        "inversion algorithm mapping articles to continuous 2D AllSides coordinates (Bias_x, Fact_y).",
        bold_prefix="Psycholinguistic Author Tone & Stance Modeling: "
    )
    add_bullet_p(
        doc,
        "Constructed a high-precision regex matching engine for eight informal logical fallacies (Ad Hominem, "
        "Appeal to Fear, Phantom Authority, False Dilemma, etc.) with zero hallucination and an aggregated Fallacy Severity Index (FSI).",
        bold_prefix="Deterministic Cognitive Fallacy Audit: "
    )
    add_bullet_p(
        doc,
        "Implemented sentence-by-sentence cross-referencing against verified consensus data from the World "
        "Health Organization (WHO), CDC, NASA, and IPCC, backed by dynamic Wikipedia OpenSearch API lookups.",
        bold_prefix="Line-Level Institutional Fact Grounding: "
    )
    add_bullet_p(
        doc,
        "Combined Random Forest and XGBoost base estimators with a regularized Logistic Meta-Learner "
        "over a 5,028-dimensional fused feature space, attaining 98.33% classification accuracy, 0.9833 Macro-F1, and 0.9989 ROC-AUC "
        "on a balanced 1,200-article corpus.",
        bold_prefix="Calibrated Stacking Machine Learning: "
    )
    add_bullet_p(
        doc,
        "Deployed a lightweight Flask REST microservice on Port 5001 featuring live URL scraping, dynamic "
        "BBC RSS feed ingestion, interactive AllSides pin plotting, and sentence-level deception highlighting with 185ms latency.",
        bold_prefix="Real-Time Telemetry Dashboard: "
    )

    add_heading_2(doc, "7.2 Critical Limitations of the Current Implementation")
    add_body_p(
        doc,
        "While the Evidence and Framing Auditor achieves state-of-the-art predictive accuracy and forensic transparency, several "
        "inherent technical limitations must be acknowledged:"
    )
    add_bullet_p(
        doc,
        "The feature extraction pipelines, syllable heuristics, and fallacy lexicons are optimized strictly for "
        "English prose. The current system cannot natively audit regional languages or multilingual texts without translation preprocessing.",
        bold_prefix="Language Boundary: "
    )
    add_bullet_p(
        doc,
        "Modern deceptive campaigns frequently employ multimodal manipulation—such as pairing an authentic "
        "text with an AI-generated or context-shifted photograph. The current architecture evaluates textual modalities only.",
        bold_prefix="Unimodal Text Limitation: "
    )
    add_bullet_p(
        doc,
        "While the institutional fact matrix covers foundational public health, climate, and astronomical consensus, "
        "it relies on a curated database that requires periodic editorial synchronization with emerging scientific literature.",
        bold_prefix="Static Institutional Knowledge Boundaries: "
    )
    add_bullet_p(
        doc,
        "Heavily obfuscated news websites that render articles entirely through client-side React/Vue JavaScript "
        "or enforce strict CAPTCHA paywalls can prevent BeautifulSoup4 from extracting clean DOM text.",
        bold_prefix="JavaScript-Heavy Web Scraping Obstacles: "
    )

    add_heading_2(doc, "7.3 Multi-Phase Future Enhancement Roadmap")
    add_body_p(
        doc,
        "To extend the capabilities of the Evidence and Framing Auditor, a four-phase future research and engineering roadmap is planned:"
    )
    add_bullet_p(
        doc,
        "Incorporate OpenAI CLIP embeddings and Vision Transformers (ViT) into a dual-stream vision-text "
        "architecture to cross-verify headline claims against image contents, detecting synthetic images, deepfakes, and misattributed photos.",
        bold_prefix="Phase 1: Multimodal Vision-Language Cross-Verification: "
    )
    add_bullet_p(
        doc,
        "Integrate multilingual language models (mBERT, XLM-RoBERTa, IndicBERT) to extend stylometric and "
        "bias analysis into regional Indian languages (Hindi, Bengali, Tamil), combating vernacular misinformation on messaging platforms.",
        bold_prefix="Phase 2: Cross-Lingual & Vernacular Disinformation Auditing: "
    )
    add_bullet_p(
        doc,
        "Transition from static institutional consensus tables to dynamic SPARQL query endpoints "
        "connecting directly to live Wikidata and DBpedia knowledge graphs, enabling autonomous real-time verification of emerging breaking claims.",
        bold_prefix="Phase 3: Autonomous Live Knowledge Graph Ingestion: "
    )
    add_bullet_p(
        doc,
        "Package the client-side telemetry engine into a Chrome WebExtension and Mozilla Add-on, "
        "allowing journalists, students, and citizens to receive instantaneous veracity audits and fallacy warnings while browsing social media.",
        bold_prefix="Phase 4: Browser Extension & Edge Deployment: "
    )

    add_heading_2(doc, "7.4 Concluding Perspectives")
    add_body_p(
        doc,
        "In an era where generative AI allows fabricated realities to be manufactured at machine speed, human society cannot afford "
        "to rely on uninterpretable black-box detectors that replace one mystery with another. The Evidence and Framing Auditor proves "
        "that mathematical rigor, psycholinguistic modeling, and open institutional grounding can be harmoniously fused into an "
        "accurate, explainable, and accessible digital forensics architecture. By empowering newsrooms, fact-checkers, and everyday "
        "citizens with transparent diagnostic evidence, this project makes a tangible contribution toward restoring digital trust "
        "and protecting the integrity of human public discourse."
    )
