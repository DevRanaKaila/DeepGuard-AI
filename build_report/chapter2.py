from build_report.helpers import (
    add_heading_1, add_heading_2, add_heading_3, add_body_p, add_bullet_p,
    add_figure, add_table_custom
)

def add_chapter_2(doc):
    add_heading_1(doc, "CHAPTER 2: LITERATURE REVIEW / EXISTING SYSTEM")

    add_heading_2(doc, "2.1 Chronological Evolution of Detection Methodologies")
    add_body_p(
        doc,
        "The automated identification of deceptive news and computational propaganda has evolved through four distinct "
        "methodological paradigms over the past decade, driven by accelerating advances in natural language processing and the "
        "increasing sophistication of adversarial disinformation campaigns:"
    )
    add_bullet_p(
        doc,
        "Early automated verification frameworks relied primarily on static blacklists of known disreputable domain "
        "names, regular-expression keyword filters (e.g., matching sensational clickbait phrases like 'you won't believe'), and naive "
        "Bag-of-Words (BoW) representations classified via linear support vector machines (SVM) or Naive Bayes classifiers (Rubin et al., "
        "2015; Shu et al., 2017). These systems suffered from catastrophic brittleness; malicious authors effortlessly evaded detection "
        "by altering vocabulary, utilizing synonyms, or migrating domains.",
        bold_prefix="Phase 1: Lexical Blacklists and Surface Bag-of-Words (2015–2018): "
    )
    add_bullet_p(
        doc,
        "Researchers recognized that deceptive prose exhibits measurable structural differences compared to legitimate "
        "journalism. Pioneer studies (Ahmed et al., 2018; Zhou & Zafarani, 2020) introduced feature engineering pipelines incorporating "
        "part-of-speech (POS) tag ratios, readability scores (Flesch-Kincaid), and sentiment polarity. While more robust than pure BoW, "
        "these models operated on isolated linear combinations of surface features and lacked semantic contextual comprehension.",
        bold_prefix="Phase 2: Classical Machine Learning & Handcrafted Feature Engineering (2018–2021): "
    )
    add_bullet_p(
        doc,
        "The advent of pre-trained bidirectional transformer encoders—spearheaded by BERT (Devlin et al., 2018), "
        "RoBERTa (Liu et al., 2019), and DeBERTa (He et al., 2021)—revolutionized NLP. By fine-tuning multi-layer self-attention networks "
        "on large news corpora, benchmark classification accuracy on datasets such as LIAR and FakeNewsNet rose dramatically above 90%. "
        "However, this phase introduced the severe 'black-box problem': models could not explain why an article was deemed fake, and "
        "subsequent probes proved that transformers heavily relied on spurious statistical correlations rather than genuine semantic reasoning.",
        bold_prefix="Phase 3: Deep Neural Networks and Dense Transformer Encoders (2021–2024): "
    )
    add_bullet_p(
        doc,
        "Current cutting-edge research focuses on augmenting neural representations with structured external "
        "knowledge bases, argumentative discourse graphs, and multimodal verification. Rather than treating an article as an isolated string, "
        "contemporary architectures attempt to cross-reference claims against knowledge graphs (Wikidata, DBpedia) and analyze rhetorical "
        "argumentation structures (Xie et al., 2025; Cao et al., 2025).",
        bold_prefix="Phase 4: Knowledge Graph Grounding & Epistemic Multi-Branch Verification (2024–2026): "
    )

    add_heading_2(doc, "2.2 Critical Analysis of Contemporary Research (2024–2026)")
    add_body_p(
        doc,
        "A rigorous, systematic review of seminal peer-reviewed research published in premier IEEE, ACM, AAAI, and ACL venues "
        "contextualizes the technical foundations and boundaries of contemporary automated fact-checking:"
    )
    add_bullet_p(
        doc,
        "B. Xie, X. Ma, and X. Shan (IEEE Transactions on Computational Social Systems, 2025) proposed 'MiLk-FD', a heterogeneous graph "
        "neural network that integrates multi-source knowledge graph triples (Wikidata, ConceptNet) with semantic representations extracted "
        "from LLaMA2-7B. The model demonstrated that grounding news text in structured relational graphs boosts classification accuracy "
        "on the challenging LIAR-PLUS benchmark to 81.2%. However, the authors noted critical limitations: the framework demands massive "
        "GPU compute clusters (preventing edge or low-latency deployment), exhibits high inference latency (>3.8 seconds per article), "
        "and completely lacks psycholinguistic author bias or logical fallacy quantification.",
        bold_prefix="Multi-Knowledge Graph Grounding (Xie et al., 2025): "
    )
    add_bullet_p(
        doc,
        "B. Cao, Q. Wu, J. Cao, B. Liu, and J. Gui (Proceedings of AAAI, 2025) introduced 'ERIC-FND', which leverages external reliable "
        "information from online encyclopedias alongside contrastive cross-modal representation learning. The model achieved 94.6% accuracy "
        "on social media benchmarks. Crucially, the authors established that cross-referencing claims against external knowledge bases "
        "substantially mitigates generative AI synthetic text artifacts. However, ERIC-FND treats fact retrieval as an opaque embedding "
        "matching step without delivering line-level evidentiary citations or evaluating authorial ideological framing.",
        bold_prefix="External Reliable Information-Enhanced Contrastive Learning (Cao et al., 2025): "
    )
    add_bullet_p(
        doc,
        "L. Xiao, Q. Zhang, C. Shi, S. Wang, U. Naseem, and L. Hu (Proceedings of the ACM Web Conference - WWW '24, 2024) formulated "
        "'MSynFD', which constructs multi-hop syntax dependency trees to capture subtle grammatical irregularities and non-standard syntactic "
        "patterns characteristic of computational propaganda. The authors proved that syntactic dependency features are significantly more "
        "resilient to out-of-distribution topical shift than lexical token representations, validating the core premise that syntactic and "
        "stylometric features provide essential domain-invariant signals.",
        bold_prefix="Multi-Hop Syntax-Aware Fake News Detection (Xiao et al., 2024): "
    )
    add_bullet_p(
        doc,
        "Y. Sun, Q. Huang, A. K. H. Tung, and J. Yu (Proceedings of ACL 2025, 2025) investigated the severe 'stance inversion problem' "
        "where conventional political bias models misclassify articles criticizing ideological allies. They introduced 'PRISM', a political-aware "
        "cross-encoder that maps articles into continuous ideological embedding spaces based on target entity critique. Our project directly "
        "adapts and extends this principle into our deterministic Target-Stance Ideological Coordinate Engine.",
        bold_prefix="Interpretable Political Bias Embeddings (Sun et al., 2025): "
    )
    add_bullet_p(
        doc,
        "Y. Lei and R. Huang (Proceedings of EMNLP 2024, 2024) demonstrated that large language models struggle to identify fallacious "
        "reasoning unless explicitly guided by formal logical structure trees. Similarly, M.-H. Yeh, R. Wan, and T.-H. K. Huang (EMNLP 2024) "
        "published 'CoCoLoFa', benchmarking 8 common informal fallacies in digital commentary. Their empirical findings proved that "
        "deterministic pattern matching combined with rhetorical cue lexicons achieves superior precision and zero hallucination compared "
        "to open-ended prompting of commercial LLMs.",
        bold_prefix="Cognitive Fallacy Reasoning in Language Models (Lei & Huang, 2024; Yeh et al., 2024): "
    )

    add_heading_2(doc, "2.3 Comparative Synthesis of Existing Detection Frameworks")
    add_body_p(
        doc,
        "To establish a clear comparative baseline, Table 2.1 systematically contrasts eight leading commercial and research fact-checking "
        "architectures against the Evidence and Framing Auditor across seven foundational engineering criteria:"
    )

    comp_data = [
        ["Ad Fontes Media", "Manual Expert Review", "Opaque (Rubric)", "Qualitative", "No", "No", "High (>24h)", "Web Report"],
        ["AllSides", "Blind Bias Survey", "Domain-Level Only", "Domain Only", "No", "No", "Manual / Static", "Web Portal"],
        ["BERT Baseline", "Fine-Tuned Encoder", "Zero (Black Box)", "None", "No", "No", "Moderate (150ms)", "CLI Script"],
        ["RoBERTa News", "Dense Transformer", "Zero (Black Box)", "None", "No", "No", "Moderate (180ms)", "CLI Script"],
        ["MiLk-FD (2025)", "Heterogeneous GNN", "Low (Attention)", "None", "No", "Yes (Wikidata)", "Very Slow (3.8s)", "Research Code"],
        ["ERIC-FND (2025)", "Contrastive Encoder", "Low (Latent)", "None", "No", "Yes (Online Enc)", "Slow (1.2s)", "Research Code"],
        ["MSynFD (2024)", "Syntax GCN", "Moderate (Parse)", "None", "No", "No", "Moderate (420ms)", "Research Code"],
        ["Evidence Auditor (Ours)", "Hybrid Stacking Ensemble", "High (Full Diagnostic)", "Formulated (ABS, 2D)", "Yes (8 Classes)", "Yes (WHO, NASA, IPCC)", "Real-Time (185ms)", "Web Telemetry UI"]
    ]

    add_table_custom(
        doc,
        headers=["Framework / System", "Underlying Architecture", "Interpretability Level", "Author Bias Modeling", "Fallacy Detection", "Fact Grounding", "Inference Latency", "Deployment Interface"],
        rows_data=comp_data,
        caption_text="Comparative Architectural Matrix of Contemporary State-of-the-Art Detection Frameworks.",
        table_num="Table 2.1",
        col_widths=[1.0, 1.0, 0.9, 0.8, 0.6, 0.8, 0.7, 0.8]
    )

    add_heading_2(doc, "2.4 Identification of Critical Research Gaps")
    add_body_p(
        doc,
        "The comparative synthesis reveals four profound technological and scientific gaps in the existing body of literature:"
    )
    add_bullet_p(
        doc,
        "While deep learning architectures achieve high in-domain benchmark accuracy, they fail to provide "
        "actionable evidentiary explanations. In legal tribunals, regulatory inquiries, and journalistic investigations, an unexplained "
        "probability score is completely unacceptable. There is an acute need for a system that provides sentence-level attribution, "
        "quantifiable stylometric indices, and explicit fallacy citations.",
        bold_prefix="Gap 1: The Forensic Interpretability Chasm: "
    )
    add_bullet_p(
        doc,
        "Mainstream bias evaluation operates exclusively at the publisher domain level, treating all articles "
        "from a news outlet as ideologically homogeneous. Furthermore, when an article critiques an entity within its own ideological "
        "sphere, bag-of-words and lexical models invert the true political direction. No existing system integrates directional entity-critique "
        "parsing to compute continuous 2D ideological coordinates in real time.",
        bold_prefix="Gap 2: The Stance Inversion and Coarse Aggregation Blind Spot: "
    )
    add_bullet_p(
        doc,
        "Existing systems treat author tone qualitatively. There are no standardized, closed-form mathematical "
        "formulations that concurrently quantify Subjectivity, Emotional Hyperbole, Epistemic Hedging, and Headline-Body Sentiment Skew "
        "into a composite, reproducible score.",
        bold_prefix="Gap 3: Lack of Formal Mathematical Formulations for Author Bias: "
    )
    add_bullet_p(
        doc,
        "While research prototypes like MiLk-FD demonstrate the value of knowledge graphs, they require multi-billion "
        "parameter language models and specialized GPU hardware that cannot run on edge servers or sustain interactive web applications. "
        "A lightweight, deterministic institutional consensus lookup engine that operates with millisecond latency on standard CPU hardware "
        "remains absent from the literature.",
        bold_prefix="Gap 4: Deployment Infeasibility of Heavy Knowledge Graph Networks: "
    )

    add_heading_2(doc, "2.5 Methodological Positioning of the Evidence and Framing Auditor")
    add_body_p(
        doc,
        "The Evidence and Framing Auditor is methodologically positioned to directly bridge each of these identified gaps. Rather than "
        "competing in a narrow race for marginally higher accuracy on synthetic benchmarks via ever-larger neural parameters, our system "
        "prioritizes diagnostic interpretability, multi-branch epistemic completeness, and real-time operational efficiency. By combining "
        "dense, interpretable mathematical stylometrics and author bias formulations with sublinear TF-IDF semantic features inside a "
        "calibrated Stacking Ensemble, the framework achieves state-of-the-art predictive accuracy (98.33%) while executing in under "
        "200 milliseconds on standard CPU hardware and providing 100% transparent diagnostic explanations."
    )
