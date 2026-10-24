from build_report.helpers import (
    add_heading_1, add_heading_2, add_heading_3, add_body_p, add_bullet_p,
    add_equation_p, add_figure, add_table_custom
)

def add_chapter_1(doc):
    add_heading_1(doc, "CHAPTER 1: INTRODUCTION")

    add_heading_2(doc, "1.1 Background and Societal Motivation")
    add_body_p(
        doc,
        "In the contemporary digital information ecosystem, the rapid democratization and global interconnectivity of "
        "social networking architectures, online news aggregators, and decentralized publishing platforms have revolutionized "
        "how human society consumes, disseminates, and engages with information. However, this frictionless dissemination "
        "paradigm has simultaneously catalyzed an unprecedented epistemological crisis: the industrialized propagation of "
        "hyper-partisan disinformation, synthesized deceptive reports, and deliberate epistemic distortions. According to "
        "foundational empirical risk assessments conducted by UNESCO (2025) and the World Economic Forum Global Risks Report "
        "(2024–2025), misinformation and digital deception now rank as the single greatest short-term risk to global societal "
        "stability, eclipsing even conventional macroeconomic volatility and extreme geopolitical turbulence."
    )
    add_body_p(
        doc,
        "The societal consequences of unchecked digital deception are catastrophic and systemic. In the civic sphere, targeted "
        "disinformation campaigns systematically erode public confidence in democratic institutions, degrade voter consensus, "
        "and polarize populations across deep socio-political fault lines. During geopolitical conflicts, belligerents weaponize "
        "coordinated computational propaganda to manipulate international perceptions and obscure humanitarian atrocities. In the "
        "realm of public health—exemplified during the COVID-19 pandemic and subsequent global vaccination efforts—fabricated medical "
        "panaceas, unsubstantiated vaccine microchip conspiracies, and manufactured institutional distrust resulted in direct loss "
        "of human life and the revival of previously eradicated infectious pathologies. Furthermore, in commercial markets, synthetic "
        "news releases detailing fabricated corporate insolvencies or fictitious acquisitions have induced flash-crashes, wiping out "
        "billions of dollars in market capitalization within seconds."
    )
    add_body_p(
        doc,
        "This crisis has been exponentially intensified by the recent democratization of high-capacity generative artificial "
        "intelligence, particularly Large Language Models (LLMs) such as OpenAI GPT-4, Meta LLaMA-3, and Google Gemini. "
        "Historically, fabricated news could often be identified through surface-level artifacts such as blatant spelling errors, "
        "broken grammatical structures, or crude typographical anomalies. Contemporary generative AI pipelines, however, have "
        "lowered the marginal cost of producing syntactically flawless, grammatically pristine, and stylistically convincing deceptive "
        "prose to near zero. Malicious actors can now synthesize thousands of persuasive, tailored disinformation articles in minutes, "
        "completely overwhelming manual fact-checking organizations and rendering traditional keyword-based blacklists and surface "
        "heuristics obsolete."
    )

    add_heading_2(doc, "1.2 The Deception Spectrum & Linguistic Manipulations")
    add_body_p(
        doc,
        "Automated veracity assessment cannot be treated as a trivial binary text-classification task. Digital misinformation does "
        "not operate as an undifferentiated monolith; rather, it manifests across a multifaceted continuum known as the "
        "Deception Spectrum. Deceptive prose exploits subtle cognitive vulnerabilities through complex rhetorical framing, psychological "
        "nudging, and contextual manipulation. A rigorous forensic architecture must systematically decompose and identify each "
        "constituent phenomenon across this spectrum:"
    )
    add_bullet_p(
        doc,
        "Disinformation campaigns deliberately utilize hyperbolic language, inflammatory adjectives, and "
        "provocative phrasing designed to trigger acute moral outrage, fear, or cognitive panic. Emotional over-saturation impairs "
        "critical analytical thinking, inducing readers to immediately share deceptive content before evaluating its empirical validity.",
        bold_prefix="Affective Polarization and Sensationalism: "
    )
    add_bullet_p(
        doc,
        "Fabricated articles frequently rely on invalid rhetorical structures that simulate logical "
        "coherence while violating deductive validity. These include Ad Hominem character assassinations, False Dilemma dichotomies "
        "('either you stand with our movement or you support societal collapse'), and Phantom Authority attribution ('anonymous top "
        "whistleblowers confirm').",
        bold_prefix="Cognitive Distortions and Rhetorical Fallacies: "
    )
    add_bullet_p(
        doc,
        "The most pernicious form of contemporary misinformation does not manufacture blatant falsehoods out "
        "of whole cloth; instead, it selectively quotes authentic statistical figures or scientific excerpts while stripping away "
        "essential qualifying boundaries, confidence intervals, or foundational context, leading the reader to invalid conclusions.",
        bold_prefix="Context Stripping and Selective Omission: "
    )
    add_bullet_p(
        doc,
        "Mainstream reporting often cloaks partisan hostility under the guise of objective journalism. "
        "Deceptive framing manipulates directional verbs and evaluative modifiers when reporting on specific political figures, "
        "generating systematic ideological skew that evades keyword filters.",
        bold_prefix="Target-Stance Ideological Framing: "
    )
    add_bullet_p(
        doc,
        "Fabricated narratives frequently disguise speculation as definitive reporting through the "
        "unsubstantiated accumulation of epistemic hedging phrases ('it is rumored', 'sources claim', 'many believe'), insulating "
        "the author from direct accountability while implanting unverified claims in public discourse.",
        bold_prefix="Epistemic Uncertainty and Unsubstantiated Hedging: "
    )

    add_heading_2(doc, "1.3 Problem Statement")
    add_body_p(
        doc,
        "Despite extensive research into computational fact-checking and automated fake news detection, existing computational "
        "methodologies exhibit foundational architectural flaws that severely constrain their real-world utility and legal admissibility:"
    )
    add_bullet_p(
        doc,
        "Contemporary deep learning detectors predominantly rely on fine-tuned transformer encoders "
        "(e.g., BERT, RoBERTa, DeBERTa). While these models achieve commendable accuracy on in-distribution academic benchmark "
        "corpora, they operate as uninterpretable mathematical black boxes. They output a raw probability score (e.g., '0.94 Fake') "
        "without providing any verifiable linguistic evidence, reasoning traces, or diagnostic attribution. In forensic journalism, "
        "editorial newsrooms, and regulatory compliance tribunals, opaque probability outputs are inadmissible and practically useless.",
        bold_prefix="The Forensic Interpretability Chasm: "
    )
    add_bullet_p(
        doc,
        "Transformer-based models heavily exploit spurious lexical correlations and topical shortcuts "
        "(e.g., associating specific political keywords or controversial topics with deception regardless of actual context). "
        "Consequently, when evaluated on out-of-distribution news or emerging real-world narratives, their classification accuracy "
        "catastrophically drops by 25% to 40%.",
        bold_prefix="Vulnerability to Spurious Lexical Shortcuts: "
    )
    add_bullet_p(
        doc,
        "Commercial media bias aggregators (e.g., AllSides, Ad Fontes Media) rate political "
        "bias strictly at the aggregate publisher domain level (e.g., labeling an entire publication as 'Left' or 'Right'). They "
        "fail to evaluate the specific stance, tone, and entity targeting of individual articles, completely misclassifying articles "
        "where a traditionally conservative outlet publishes an editorial criticizing a conservative candidate.",
        bold_prefix="The Stance-Inversion Blind Spot: "
    )
    add_bullet_p(
        doc,
        "Existing NLP architectures treat deception detection either as pure stylometric analysis or as pure "
        "semantic text classification. None synthesize high-dimensional stylometrics, psycholinguistic author bias formulas, "
        "deterministic cognitive fallacy scanning, and real-time institutional knowledge grounding into a unified, calibrated machine "
        "learning framework.",
        bold_prefix="Absence of Multidisciplinary Epistemic Verification: "
    )

    add_heading_2(doc, "1.4 Measurable Project Objectives")
    add_body_p(
        doc,
        "To resolve these foundational limitations, the 'Evidence and Framing Auditor' project formulates and accomplishes the "
        "following six core engineering and scientific objectives:"
    )

    obj_data = [
        ["Objective 1", "Multi-Branch Linguistic & Stylometric Engineering", "Extract and normalize 18+ mathematical stylometric metrics (Type-Token Ratio, Simpson's Diversity, Flesch Reading Ease, Flesch-Kincaid Grade Level, Gunning Fog Index, Punctuation Entropy) capturing structural signatures of deceptive prose."],
        ["Objective 2", "Psycholinguistic Author Tone & Bias Quantification", "Derive and implement closed-form mathematical equations for Subjectivity Index (S_idx), Emotional Hyperbole Factor (EHF), Hedging Uncertainty Ratio (HUR), Affective Polarization Density (APD), and Composite Author Bias Score (ABS)."],
        ["Objective 3", "Target-Stance Ideological Coordinate Formulation", "Develop a directional stance algorithm that resolves political stance inversion by cross-referencing entity mentions against attack modifiers, mapping each article to continuous 2D coordinates (Bias_x, Fact_y) on an AllSides-calibrated spectrum."],
        ["Objective 4", "Deterministic 8-Class Cognitive Fallacy Detection", "Design and benchmark a deterministic pattern-matching engine identifying 8 classes of rhetorical and logical fallacies (Ad Hominem, Appeal to Fear, Phantom Authority, False Dilemma, Cherry-Picking, etc.) with an aggregated Fallacy Severity Index (FSI)."],
        ["Objective 5", "Line-Level Institutional Knowledge Grounding", "Construct a curated, authoritative institutional knowledge matrix cross-referencing claims against official datasets from the World Health Organization (WHO), CDC, NASA CNEOS, IPCC AR6, UNESCO, and Wikipedia OpenSearch API."],
        ["Objective 6", "Calibrated Hybrid Stacking ML & Web Telemetry", "Train a hybrid stacking ensemble combining Logistic Regression, Random Forest, and XGBoost over a 5,028-dimensional fused feature space, achieving ≥98% accuracy and ≥0.99 ROC-AUC, deployed via a real-time web telemetry dashboard with live URL scraping."]
    ]
    add_table_custom(
        doc,
        headers=["Milestone", "Research & Engineering Objective", "Measurable Deliverables & Targets"],
        rows_data=obj_data,
        caption_text="Summary of Measurable Engineering Objectives and Quantitative Milestones.",
        table_num="Table 1.1",
        col_widths=[1.1, 2.0, 2.67]
    )

    add_heading_2(doc, "1.5 Scope and Operational Boundaries")
    add_body_p(
        doc,
        "The operational scope of the Evidence and Framing Auditor encompasses both automated batch processing of standardized news "
        "corpora and real-time interactive verification of live digital content. Specifically, the framework supports:"
    )
    add_bullet_p(
        doc,
        "Processing of full-length English news articles, digital blog posts, press releases, and editorial columns.",
        bold_prefix="Input Modalities: "
    )
    add_bullet_p(
        doc,
        "Real-time DOM tree parsing, CSS selector stripping, and main body text sanitization from live HTTP/HTTPS URLs.",
        bold_prefix="Live Web Ingestion: "
    )
    add_bullet_p(
        doc,
        "Dynamic polling and verification of live news streams (e.g., BBC World News RSS feed) with instant veracity telemetry.",
        bold_prefix="Automated RSS Feed Monitoring: "
    )
    add_bullet_p(
        doc,
        "Complete mathematical audit reporting every extracted metric, 2D ideological coordinates, sentence-level fallacy triggers, and institutional contradiction alerts.",
        bold_prefix="Diagnostic Telemetry: "
    )
    add_body_p(
        doc,
        "The project boundaries explicitly delimit the current version to English-language digital texts; multi-lingual transfer and "
        "cross-modal image verification (e.g., deepfake image-text consistency) are designated as future extensions."
    )

    add_heading_2(doc, "1.6 Organization of the Report")
    add_body_p(
        doc,
        "This project report is structured into seven comprehensive chapters following the official AKTU guidelines:"
    )
    add_bullet_p(doc, "Articulates the background, problem statement, objectives, scope, and technical terminology.", bold_prefix="Chapter 1 (Introduction): ")
    add_bullet_p(doc, "Provides a critical, chronological review of existing deception detection literature (2015–2026), comparative matrices, and identified research gaps.", bold_prefix="Chapter 2 (Literature Review): ")
    add_bullet_p(doc, "Presents the high-level system architecture, closed-form mathematical equations, feasibility studies, requirements, and UML/DFD models.", bold_prefix="Chapter 3 (System Analysis and Design): ")
    add_bullet_p(doc, "Details the modular Python implementation, software stack, core algorithms, and optimization strategies.", bold_prefix="Chapter 4 (Implementation): ")
    add_bullet_p(doc, "Presents the testing methodology, unit test suites, formal test cases matrix, adversarial testing, and security auditing.", bold_prefix="Chapter 5 (Testing): ")
    add_bullet_p(doc, "Analyzes empirical performance on the benchmark corpus, comparative model evaluations, ablation studies, confusion matrices, and qualitative case studies.", bold_prefix="Chapter 6 (Results and Discussion): ")
    add_bullet_p(doc, "Summarizes project deliverables, acknowledges technical constraints, and outlines a concrete four-phase future roadmap.", bold_prefix="Chapter 7 (Conclusion and Future Scope): ")
    add_bullet_p(doc, "Followed by standard IEEE References and comprehensive Technical Appendices.", bold_prefix="Back Matter: ")
