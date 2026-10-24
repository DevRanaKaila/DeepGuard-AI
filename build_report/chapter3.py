from build_report.helpers import (
    add_heading_1, add_heading_2, add_heading_3, add_body_p, add_bullet_p,
    add_equation_p, add_figure, add_table_custom
)

def add_chapter_3(doc):
    add_heading_1(doc, "CHAPTER 3: SYSTEM ANALYSIS AND DESIGN")

    add_heading_2(doc, "3.1 High-Level Multi-Branch System Architecture")
    add_body_p(
        doc,
        "The Evidence and Framing Auditor is architected as an end-to-end, multi-tier Natural Language Processing and Digital "
        "Forensics system. In contrast to conventional monolithic neural architectures that pass raw token sequences directly "
        "into an uninterpretable deep neural network, our framework employs an orthogonal, multi-branch decomposition paradigm. "
        "Every incoming document—whether submitted as raw text, ingested via real-time web URL scraping, or parsed from a dynamic "
        "RSS feed—is concurrently analyzed across five specialized analytical engines:"
    )
    add_bullet_p(doc, "Extracts 18+ mathematical metrics capturing lexical richness, vocabulary diversity, syntactic complexity, and cognitive readability.", bold_prefix="Branch 1 (Stylometric & Lexical Diversity Engine): ")
    add_bullet_p(doc, "Computes formulated psycholinguistic metrics quantifying authorial subjectivity, emotional hyperbole, epistemic hedging, and directional 2D AllSides political coordinates.", bold_prefix="Branch 2 (Author Tone & Ideological Stance Engine): ")
    add_bullet_p(doc, "Generates 5,000 sublinear TF-IDF unigram and bigram features capturing high-dimensional topical and lexical context.", bold_prefix="Branch 3 (Sublinear Semantic Embeddings): ")
    add_bullet_p(doc, "Executes deterministic compiled regular expressions to identify eight formal classes of rhetorical distortion and calculates an aggregated Fallacy Severity Index (FSI).", bold_prefix="Branch 4 (Cognitive Fallacy Scanner): ")
    add_bullet_p(doc, "Cross-references claims sentence-by-sentence against curated institutional consensus databases (WHO, CDC, NASA, IPCC, UNESCO) and resolves entities via the Wikipedia OpenSearch API.", bold_prefix="Branch 5 (Line-Level Institutional Fact Grounding): ")

    add_figure(
        doc,
        "presentation/assets_fake_news/fig1_system_architecture.png",
        "High-Level Multi-Branch System Architecture of the Evidence and Framing Auditor.",
        fig_num="Fig. 3.1",
        width_in=5.4
    )

    add_body_p(
        doc,
        "As illustrated in Figure 3.1, the dense outputs of Branch 1, Branch 2, and Branch 4 (28 engineered numerical features) "
        "are normalized using a standard Z-score scaler and concatenated with the 5,000 sparse TF-IDF features of Branch 3, creating "
        "a fused 5,028-dimensional feature representation. This fused representation is fed into a calibrated Stacking Ensemble "
        "classifier combining Random Forest, XGBoost, and a regularized Logistic Meta-Learner to output the final authenticity verdict."

    )

    add_heading_2(doc, "3.2 Detailed Mathematical Formulations of Analytical Engines")
    add_body_p(
        doc,
        "A foundational requirement of forensic credibility is mathematical rigor and transparency. Below are the formal "
        "closed-form equations governing each of the five analytical branches:"
    )

    add_heading_3(doc, "3.2.1 Branch 1: High-Dimensional Stylometrics & Lexical Diversity Engine")
    add_body_p(
        doc,
        "Let a sanitized document D consist of a sequence of N total word tokens and V distinct unique vocabulary tokens. "
        "To rigorously quantify lexical richness and vocabulary degradation typical of hasty, automated, or deceptive writing, "
        "the engine implements four complementary variants of the Type-Token Ratio:"
    )
    add_equation_p(doc, "TTR = V / N", eq_num="3.1")
    add_equation_p(doc, "RTTR = V / sqrt(N)", eq_num="3.2")
    add_equation_p(doc, "CTTR = V / sqrt(2N)", eq_num="3.3")
    add_equation_p(doc, "BiTTR = log(V) / log(N)", eq_num="3.4")
    add_body_p(
        doc,
        "While standard TTR exhibits high sensitivity to text length, the Root TTR (RTTR) and Bilogarithmic TTR (BiTTR) provide "
        "length-invariant stability. To evaluate extreme lexical scarcity, the engine calculates the frequency of Hapax Legomena "
        "(words occurring exactly once, V_1) and Dis Legomena (words occurring exactly twice, V_2):"
    )
    add_equation_p(doc, "HLR = V_1 / N,          DLR = V_2 / N", eq_num="3.5")
    add_body_p(
        doc,
        "To capture the concentration and evenness of vocabulary distribution, the framework computes Simpson's Diversity Index (D_simpson) "
        "and Shannon's Information Lexical Entropy (H_lex):"
    )
    add_equation_p(doc, "D_simpson = 1 - sum( n_i * (n_i - 1) ) / ( N * (N - 1) )", eq_num="3.6")
    add_equation_p(doc, "H_lex = - sum( p_i * log_2(p_i) ),   where p_i = n_i / N", eq_num="3.7")
    add_body_p(
        doc,
        "Higher lexical entropy indicates rich, nuanced vocabulary characteristic of investigative journalism, whereas low entropy "
        "signifies repetitive, formulaic propaganda. Furthermore, the engine computes five standardized cognitive readability metrics, "
        "where ASL is Average Sentence Length (words per sentence), ASW is Average Syllables per Word, CW is Complex Words (>= 3 syllables), "
        "L is average characters per 100 words, and S is average sentences per 100 words:"
    )
    add_equation_p(doc, "FRE = 206.835 - (1.015 * ASL) - (84.6 * ASW)", eq_num="3.8")
    add_equation_p(doc, "FKGL = (0.39 * ASL) + (11.8 * ASW) - 15.59", eq_num="3.9")
    add_equation_p(doc, "GFI = 0.4 * ( ASL + 100 * (CW / N) )", eq_num="3.10")
    add_equation_p(doc, "ARI = 4.71 * (chars / N) + 0.5 * (N / sentences) - 21.43", eq_num="3.11")
    add_equation_p(doc, "CLI = 0.0588 * L - 0.296 * S - 15.8", eq_num="3.12")
    add_body_p(
        doc,
        "Finally, syntactic agitation is captured via Punctuation Entropy over exclamation marks, question marks, quotation marks, and commas:"
    )
    add_equation_p(doc, "H_punct = - sum( q_k * log_2(q_k) ),   where q_k = count(punct_k) / sum(punct)", eq_num="3.13")

    styl_tbl = [
        ["TTR, RTTR, BiTTR", "Lexical diversity & richness", "[0.0, 1.0]", "Lower in repetitive propaganda"],
        ["Hapax / Dis Legomena", "Rare vocabulary utilization", "[0.0, 1.0]", "High in scholarly journalism"],
        ["Simpson's Diversity (D)", "Evenness of lexical usage", "[0.0, 1.0]", "Suppressed in deceptive text"],
        ["Shannon Entropy (H_lex)", "Information density of words", "[0.0, 12.0]", "Reflects semantic complexity"],
        ["Flesch Reading Ease", "Cognitive fluency / accessibility", "[-30, 100]", "Very low or very high in clickbait"],
        ["Flesch-Kincaid Grade", "Required US educational grade", "[0.0, 20.0]", "Clickbait targets grade <= 6"],
        ["Punctuation Entropy", "Syntactic agitation & structure", "[0.0, 3.0]", "High in sensationalist hysteria"]
    ]
    add_table_custom(
        doc,
        headers=["Metric Name", "Mathematical Significance", "Value Range", "Forensic Indicator in News"],
        rows_data=styl_tbl,
        caption_text="Mathematical Formulations and Epistemic Interpretations of Stylometric Indices.",
        table_num="Table 3.1",
        col_widths=[1.5, 1.5, 1.0, 1.77]
    )

    add_heading_3(doc, "3.2.2 Branch 2: Psycholinguistic Author Tone & Ideological Stance Engine")
    add_body_p(
        doc,
        "Deceptive authors introduce subtle psychological manipulations into news reporting. Branch 2 evaluates five formulated "
        "psycholinguistic indices and calculates continuous 2D coordinates on an AllSides ideological spectrum:"
    )
    add_bullet_p(
        doc,
        "Evaluated via TextBlob sentiment polarity analysis, quantifying the proportion of subjective judgment vs objective fact:",
        bold_prefix="Subjectivity Index (S_idx): "
    )
    add_equation_p(doc, "S_idx = sum( subjectivity(sentence_i) ) / N_sentences,   S_idx in [0.0, 1.0]", eq_num="3.14")
    add_bullet_p(
        doc,
        "Measures the density of sensational modifiers and emotional intensifiers normalized by word count:",
        bold_prefix="Emotional Hyperbole Factor (EHF): "
    )
    add_equation_p(doc, "EHF = ( ( count(L_sensational) + 1.5 * count(L_intensifiers) ) / N ) * 100", eq_num="3.15")
    add_bullet_p(
        doc,
        "Measures the frequency of speculative hedging phrases ('allegedly', 'sources claim', 'many believe'):",
        bold_prefix="Hedging Uncertainty Ratio (HUR): "
    )
    add_equation_p(doc, "HUR = count(L_hedges) / max(1, N_sentences)", eq_num="3.16")
    add_bullet_p(
        doc,
        "Measures variance in sentiment polarity across individual sentences, capturing dramatic emotional swings:",
        bold_prefix="Affective Polarization Density (APD): "
    )
    add_equation_p(doc, "APD = sum( | polarity(sentence_i) - mu_polarity | ) / N_sentences", eq_num="3.17")
    add_bullet_p(
        doc,
        "Integrates S_idx, EHF, HUR, and headline-body sentiment divergence (Delta_pol) into a calibrated 0–100 scale:",
        bold_prefix="Composite Author Bias Score (ABS): "
    )
    add_equation_p(doc, "ABS = min(100, 0.35 * (S_idx * 100) + 0.30 * EHF + 0.20 * (HUR * 50) + 0.15 * (Delta_pol * 50))", eq_num="3.18")

    add_body_p(
        doc,
        "Directional Target-Stance Ideological Inversion Algorithm: Standard political bias classifiers fail when an article "
        "mentions political entities in an adversarial context (e.g., an article criticizing conservative policies is conservative "
        "in entity keywords but left-leaning in stance). Our algorithm resolves this by identifying political entities E, evaluating "
        "directional attack modifiers A and praise modifiers P within a 5-token context window, and computing continuous coordinates:"
    )
    add_equation_p(doc, "Stance_left = count(E_left, P) + count(E_right, A)", eq_num="3.19")
    add_equation_p(doc, "Stance_right = count(E_right, P) + count(E_left, A)", eq_num="3.20")
    add_equation_p(doc, "Bias_x = (Stance_right - Stance_left) / max(1, Stance_right + Stance_left),   Bias_x in [-1.0, 1.0]", eq_num="3.21")
    add_equation_p(doc, "Fact_y = 1.0 - (ABS / 100) * 0.5 - (FSI / 100) * 0.5,   Fact_y in [0.0, 1.0]", eq_num="3.22")

    add_heading_3(doc, "3.2.3 Branch 3: Sublinear Semantic N-Gram Vectorization")
    add_body_p(
        doc,
        "To capture broad semantic context and vocabulary patterns without allowing frequent words to dominate the feature space, "
        "Branch 3 applies sublinear Term Frequency – Inverse Document Frequency (TF-IDF) scaling across unigrams and bigrams "
        "(n-gram range 1–2, max_features=5,000, sublinear_tf=True):"
    )
    add_equation_p(doc, "tf_sublinear(t, d) = 1 + log( f_{t,d} )   if f_{t,d} > 0,   else 0", eq_num="3.23")
    add_equation_p(doc, "idf(t, D) = log( (1 + |D|) / (1 + |{d in D : t in d}|) ) + 1", eq_num="3.24")
    add_equation_p(doc, "TF-IDF(t, d, D) = tf_sublinear(t, d) * idf(t, D)", eq_num="3.25")
    add_body_p(
        doc,
        "The resulting 5,000-dimensional sparse vector is L2-normalized: v_norm = v / ||v||_2."
    )

    add_heading_3(doc, "3.2.4 Branch 4: Deterministic 8-Class Cognitive Fallacy Detection Engine")
    add_body_p(
        doc,
        "To provide forensic explainability, Branch 4 executes a library of pre-compiled regular expressions matching eight "
        "distinct informal logical and rhetorical distortions. In digital forensics, cognitive distortions represent deliberate "
        "attempts to manipulate the reader's deductive reasoning without providing empirical substantiation. Each class is defined "
        "with specific rhetorical rules and assigned an empirical severity weight w_i based on its statistical correlation with "
        "disinformation campaigns:"
    )
    add_bullet_p(
        doc,
        "Attacking the moral character, physical appearance, or motives of an individual rather than addressing their substantive argument. "
        "Triggered by terms such as 'corrupt', 'traitor', 'evil globalists', 'scumbag', 'imbecile', 'bought and paid for'. Severity weight w = 1.5.",
        bold_prefix="1. Ad Hominem (Personal Defamation): "
    )
    add_bullet_p(
        doc,
        "Exploiting existential dread, catastrophic scenarios, and imminent destruction to induce acute panic. "
        "Triggered by patterns such as 'terrifying catastrophe', 'apocalypse is near', 'imminent disaster', 'fatal consequences'. Severity weight w = 1.4.",
        bold_prefix="2. Appeal to Fear (Scaremongering): "
    )
    add_bullet_p(
        doc,
        "Fabricating consensus by citing unnamed, mysterious, or confidential sources that cannot be verified. "
        "Triggered by phrases such as 'insiders claim', 'top scientists secretly admit', 'doctors don't want you to know', 'whistleblowers report'. Severity weight w = 1.3.",
        bold_prefix="3. Vague / Phantom Authority: "
    )
    add_bullet_p(
        doc,
        "Forcing complex socio-political issues into artificial, extreme binary choices while deliberately concealing moderate alternatives. "
        "Triggered by phrases such as 'either you stand with us or', 'the only choice is', 'no alternative but to accept'. Severity weight w = 1.2.",
        bold_prefix="4. False Dilemma (Bifurcation): "
    )
    add_bullet_p(
        doc,
        "Selecting isolated, highly atypical anecdotes or unverified testimonials while systematically ignoring overarching statistical data. "
        "Triggered by phrases such as 'this one case proves', 'i know someone who tried this and', 'ignoring all clinical trials'. Severity weight w = 1.2.",
        bold_prefix="5. Cherry-Picking (Anecdotal Extrapolation): "
    )
    add_bullet_p(
        doc,
        "Extrapolating sweeping categorical assertions regarding entire populations or institutions from single, unrepresentative incidents. "
        "Triggered by universal quantifiers paired with derogatory modifiers ('all of them always lie', 'every single official is complicit'). Severity weight w = 1.1.",
        bold_prefix="6. Hasty Generalization: "
    )
    add_bullet_p(
        doc,
        "Asserting that complex societal events are secretly controlled and manipulated by malevolent clandestine organizations or shadow elites. "
        "Triggered by terms such as 'shadow government', 'secret globalist cabal', 'clandestine plot', 'covert cover-up'. Severity weight w = 1.5.",
        bold_prefix="7. Conspiracy Framing: "
    )
    add_bullet_p(
        doc,
        "Fabricating an artificial, impending deadline to coerce immediate action or viral social sharing before critical evaluation occurs. "
        "Triggered by phrases such as 'share before deleted', 'they are banning this video right now', 'act immediately or suffer'. Severity weight w = 1.3.",
        bold_prefix="8. Manufactured Urgency: "
    )

    fallacy_data = [
        ["1. Ad Hominem", "Personal insults, character defamation, slurs", "w = 1.5", "High"],
        ["2. Appeal to Fear", "Existential dread, apocalyptic panic, catastrophe", "w = 1.4", "Critical"],
        ["3. Vague / Phantom Authority", "'anonymous insiders confirm', 'doctors hide this'", "w = 1.3", "Critical"],
        ["4. False Dilemma", "'either with us or against us', binary ultimatums", "w = 1.2", "Moderate"],
        ["5. Cherry-Picking", "Anecdotal extrapolation ignoring clinical trials", "w = 1.2", "Moderate"],
        ["6. Hasty Generalization", "Sweeping categorical assertions from single instances", "w = 1.1", "Moderate"],
        ["7. Conspiracy Framing", "'secret cabal', 'shadow rulers', cover-up plots", "w = 1.5", "Critical"],
        ["8. Manufactured Urgency", "'share before banned', 'act now before deletion'", "w = 1.3", "High"]
    ]
    add_table_custom(
        doc,
        headers=["Fallacy Class", "Linguistic Definition & Trigger Pattern", "Severity Weight", "Epistemic Risk Level"],
        rows_data=fallacy_data,
        caption_text="Taxonomy of 8 Cognitive Fallacy Classes and Empirical Severity Weights.",
        table_num="Table 3.2",
        col_widths=[1.5, 2.2, 0.9, 1.17]
    )

    add_body_p(
        doc,
        "The composite Fallacy Severity Index (FSI) aggregates all detected fallacy occurrences normalized by sentence count:"
    )
    add_equation_p(doc, "FSI = min( 100, sum_{i=1}^8 [ w_i * count(fallacy_i) ] * ( 10 / max(1, N_sentences) ) )", eq_num="3.26")

    add_heading_3(doc, "3.2.5 Branch 5: Line-Level Institutional Knowledge Grounding Engine")
    add_body_p(
        doc,
        "Branch 5 evaluates claims against an authoritative institutional knowledge database cross-referencing consensus findings "
        "from the World Health Organization (WHO), CDC, National Cancer Institute (NCI), NASA Center for Near-Earth Object Studies (CNEOS), "
        "and the Intergovernmental Panel on Climate Change (IPCC AR6). Each sentence in the document is tokenized and matched against "
        "canonical claim triggers. If an exact thematic overlap is detected, the engine flags a 'Direct Factual Contradiction' with "
        "an official consensus URL and institutional refutation."
    )

    add_heading_3(doc, "3.2.6 Calibrated Hybrid Stacking Machine Learning Classifier")
    add_body_p(
        doc,
        "The final classification stage combines the discriminative power of diverse machine learning architectures through a "
        "two-tier Stacking Ensemble. Let X_fused in R^{5028} represent the concatenated feature vector:"
    )
    add_equation_p(doc, "X_fused = [ StandardScaler( X_dense ) in R^{28}  ||  X_tfidf in R^{5000} ]", eq_num="3.27")
    add_body_p(
        doc,
        "The base layer comprises two non-linear estimators with complementary decision boundaries:"
    )
    add_bullet_p(doc, "200 decision trees trained with balanced bootstrap sub-sampling, robust to feature scale differences.", bold_prefix="Base Estimator 1 (Random Forest): ")
    add_bullet_p(doc, "150 boosted trees with learning rate eta=0.08, max_depth=6, utilizing histogram-based tree splitting for fast gradient optimization.", bold_prefix="Base Estimator 2 (XGBoost): ")
    add_body_p(
        doc,
        "To prevent target data leakage and overfitting, base models generate Out-Of-Fold (OOF) cross-validation probabilities "
        "via 5-fold Stratified K-Fold splitting. The blended meta-feature vector Z in R^4 contains [ P_RF(Real), P_RF(Fake), P_XGB(Real), P_XGB(Fake) ]. "
        "The meta-classifier is an L2-regularized Logistic Regression model optimizing the binary cross-entropy loss:"
    )
    add_equation_p(doc, "min_w  (1 / 2) * w^T w + C * sum_{i=1}^M log( 1 + exp( -y_i * w^T z_i ) )", eq_num="3.28")

    add_figure(
        doc,
        "presentation/assets_fake_news/fig3_stacking_classifier.png",
        "Schematic of the Calibrated Stacking Ensemble Combining Random Forest, XGBoost, and Logistic Meta-Learner.",
        fig_num="Fig. 3.2",
        width_in=5.2
    )

    add_heading_2(doc, "3.3 System Analysis & Feasibility Evaluation")
    add_body_p(
        doc,
        "Prior to engineering implementation, a rigorous multidimensional feasibility evaluation confirmed the viability of the system:"
    )
    add_bullet_p(
        doc,
        "The complete Python 3.11 stack leverages mature, optimized libraries (Scikit-Learn, XGBoost, SciPy, NLTK). "
        "By avoiding parameter-heavy multi-billion LLM inference, the entire 5,028-feature extraction and stacking pipeline runs "
        "in ~185ms on commodity multicore CPUs with zero GPU dependency.",
        bold_prefix="Technical Feasibility: "
    )
    add_bullet_p(
        doc,
        "The system deploys as a lightweight Flask microservice (Port 5001) with responsive HTML5/CSS3 telemetry. "
        "Journalists, forensic analysts, and regular users can paste URLs or text without requiring command-line or programming expertise.",
        bold_prefix="Operational Feasibility: "
    )
    add_bullet_p(
        doc,
        "Built 100% on open-source software with zero paid API subscriptions. Operating costs are limited to standard web hosting.",
        bold_prefix="Economic Feasibility: "
    )
    add_bullet_p(
        doc,
        "The system operates strictly as an epistemological auditor providing transparent linguistic evidence and "
        "source citations. It complies with GDPR data privacy by not permanently persisting ingested text and respects digital journalism "
        "fair-use doctrines.",
        bold_prefix="Legal & Ethical Feasibility: "
    )

    add_heading_2(doc, "3.4 Software and Hardware Requirement Specifications")
    add_body_p(
        doc,
        "Table 3.3 details the functional engineering requirements (FR) and non-functional requirements (NFR) governing the system:"
    )

    req_data = [
        ["FR-01", "Multi-Source Text Ingestion", "System must accept raw text, direct article URLs, and dynamic RSS feeds."],
        ["FR-02", "Automated DOM Cleansing", "System must strip boilerplate HTML, navigation scripts, and ads from ingested URLs."],
        ["FR-03", "Stylometric Computation", "System must compute 18+ lexical richness and readability indices in under 50ms."],
        ["FR-04", "Psycholinguistic Author Bias", "System must calculate S_idx, EHF, HUR, and Composite ABS (0–100)."],
        ["FR-05", "AllSides 2D Stance Mapping", "System must compute continuous (Bias_x, Fact_y) coordinates on 2D political spectrum."],
        ["FR-06", "Cognitive Fallacy Audit", "System must scan text for 8 fallacy classes and output matched textual excerpts."],
        ["FR-07", "Institutional Fact Grounding", "System must match claims against WHO/NASA/IPCC consensus and Wikipedia API."],
        ["FR-08", "Stacking Classification", "Stacking ensemble must output calibrated probabilities for Real vs Fake."],
        ["FR-09", "Sentence-Level Attribution", "System must highlight high-risk, manipulative sentences in red/amber badges."],
        ["FR-10", "Telemetry Web Dashboard", "System must render interactive charts, gauges, and risk matrices on Port 5001."],
        ["NFR-01", "Inference Latency", "End-to-end execution latency must remain below 250 milliseconds per article."],
        ["NFR-02", "Predictive Accuracy", "Stacking ensemble accuracy must exceed 98.0% on the multi-topic benchmark corpus."],
        ["NFR-03", "Zero Hallucination", "Fallacy and institutional grounding engines must exhibit 0% hallucination."],
        ["NFR-04", "Hardware Independence", "System must run on standard commodity x86_64 CPUs without requiring a GPU."]
    ]
    add_table_custom(
        doc,
        headers=["Req ID", "Requirement Category", "Detailed Technical Specification"],
        rows_data=req_data,
        caption_text="Functional and Non-Functional Engineering Requirement Specifications.",
        table_num="Table 3.3",
        col_widths=[1.1, 1.8, 2.87]
    )

    add_heading_2(doc, "3.5 Architectural and Behavioral Modeling (UML & DFD)")
    add_body_p(
        doc,
        "The structural, behavioral, and data-flow characteristics of the system are modeled through standard UML and DFD diagrams:"
    )
    add_bullet_p(
        doc,
        "Submits unverified digital news URLs or raw press releases through the telemetry UI. Receives instant "
        "evidence attribution, sentence-level fallacy breakdowns, and institutional contradiction flags prior to story publication.",
        bold_prefix="Actor 1: Investigative Journalist / Newsroom Editor: "
    )
    add_bullet_p(
        doc,
        "Conducts deep forensic audits of viral claims. Analyzes continuous AllSides 2D ideological "
        "coordinates, cross-references Wikipedia OpenSearch citations, and exports comprehensive PDF audit dossiers.",
        bold_prefix="Actor 2: Professional Fact-Checker & Regulatory Auditor: "
    )
    add_bullet_p(
        doc,
        "Pastes online articles to verify credibility, assess emotional bias, and foster critical media literacy.",
        bold_prefix="Actor 3: General Public & Digital Media Consumer: "
    )
    add_bullet_p(
        doc,
        "Monitors system telemetry, updates institutional consensus matrices (WHO, NASA, IPCC), retrains "
        "the Stacking Ensemble on newly labeled corpora, and inspects API throughput logs.",
        bold_prefix="Actor 4: System Administrator & ML Engineer: "
    )
    add_figure(
        doc,
        "presentation/assets_fake_news/fig2_data_flow_diagram.png",
        "Data Flow Diagram Level 1: Multi-Branch Feature Extraction and Verification Pipeline.",
        fig_num="Fig. 3.3",
        width_in=5.2
    )
    add_body_p(
        doc,
        "Figure 3.3 illustrates the Level 1 Data Flow Diagram (DFD). An external entity (User, Journalist, or RSS Poller) provides "
        "an input URL or text payload. Process 1.0 (Ingestion & Normalization) sanitizes the input and produces clean token sequences. "
        "These tokens flow concurrently into Process 2.1 (Stylometric Extractor) and Process 2.2 (Author Bias & Fallacy Scanner). "
        "Process 3.0 standardizes and concatenates all features into X_fused, which Process 4.0 (Stacking Classifier) processes to "
        "generate class probabilities. Finally, Process 5.0 renders the interactive diagnostic telemetry dashboard."
    )
    add_body_p(
        doc,
        "UML Sequence Flow: When an ingestion request arrives at the Flask REST controller (`app.py`), the request handler invokes "
        "`LiveVerificationPipeline.verify_url()` or `verify_text()`. The controller dispatches parallel asynchronous worker threads: "
        "Worker 1 invokes `TextPreprocessor.clean_text()` and executes `StylometricExtractor.extract_features()`; Worker 2 invokes "
        "`AuthorBiasAnalyzer.compute_bias_profile()`; Worker 3 executes `FallacyDetector.detect_fallacies()`; and Worker 4 parses "
        "sentences through `KnowledgeGroundingEngine.verify_sentence()`. Upon completion of all workers, `FeaturePipeline.transform()` "
        "stacks the 5,028 features, queries `StackingClassifier.predict_proba()`, and constructs the JSON response packet within 185ms."
    )
