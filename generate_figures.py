import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

os.makedirs('presentation/assets_fake_news', exist_ok=True)

# 1. FIG 1: System Architecture Overview
fig, ax = plt.subplots(figsize=(13, 8), dpi=300)
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')

# Title
ax.text(50, 96, 'EVIDENCE AND FRAMING AUDITOR: SYSTEM ARCHITECTURE', 
        ha='center', va='center', fontsize=15, fontweight='bold', color='#1A365D')
ax.text(50, 92, 'Multi-Branch Epistemic Verification & Hybrid Stacking Machine Learning Pipeline', 
        ha='center', va='center', fontsize=10, fontstyle='italic', color='#4A5568')

def draw_box(ax, x, y, w, h, title, subtitle='', color='#E2E8F0', edge='#4A5568', tc='#1A202C'):
    rect = patches.FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.5,rounding_size=1.2',
                                  facecolor=color, edgecolor=edge, linewidth=1.5)
    ax.add_patch(rect)
    if subtitle:
        ax.text(x + w/2, y + h*0.62, title, ha='center', va='center', fontsize=9.5, fontweight='bold', color=tc)
        ax.text(x + w/2, y + h*0.32, subtitle, ha='center', va='center', fontsize=8, color=tc)
    else:
        ax.text(x + w/2, y + h*0.5, title, ha='center', va='center', fontsize=9.5, fontweight='bold', color=tc)

# Input
draw_box(ax, 2, 70, 18, 14, 'INPUT INGESTION', 'Raw Text / Web URL\nLive RSS Feed', '#EBF8FF', '#3182CE', '#2B6CB0')

# Preprocessing
draw_box(ax, 24, 70, 20, 14, 'TEXT PREPROCESSING', 'Unicode Normalization\nContractions & Lemmatization', '#EDF2F7', '#4A5568', '#2D3748')
ax.annotate('', xy=(24, 77), xytext=(20, 77), arrowprops=dict(arrowstyle='->', lw=2, color='#2B6CB0'))

# 5 Branches
branches = [
    ('Branch 1: Stylometric Engine', '18+ Lexical Diversity & Readability\n(TTR, Simpson D, FRE, FKGL)', '#FEFCBF', '#D69E2E', '#744210', 58),
    ('Branch 2: Author Bias & Tone', 'S_idx, EHF, HUR, APD,\nAllSides 2D Stance Coords', '#FED7D7', '#E53E3E', '#9B2C2C', 44),
    ('Branch 3: Semantic Embeddings', 'Sublinear TF-IDF N-grams\n(5,000 Unigrams & Bigrams)', '#E9D8FD', '#805AD5', '#553C9A', 30),
    ('Branch 4: Cognitive Fallacies', '8 Rhetorical Distortion Patterns\nFallacy Severity Index (FSI)', '#FEEBC8', '#DD6B20', '#7B341E', 16),
    ('Branch 5: Institutional Truth', 'WHO, CDC, NASA, IPCC Consensus\nWikipedia OpenSearch API', '#C6F6D5', '#38A169', '#22543D', 2)
]

for title, sub, bg, border, tc, y in branches:
    draw_box(ax, 48, y, 24, 10, title, sub, bg, border, tc)
    ax.annotate('', xy=(48, y + 5), xytext=(34, 70), 
                arrowprops=dict(arrowstyle='->', lw=1.2, color='#4A5568'))

# Fusion
draw_box(ax, 76, 32, 22, 22, 'HYBRID FEATURE FUSION', 'StandardScaler (Dense 28)\n+ Sparse TF-IDF (5,000)\n= 5,028-Dim Fused Vector', '#E2E8F0', '#4A5568', '#1A202C')

for _, _, _, _, _, y in branches:
    ax.annotate('', xy=(76, 43), xytext=(72, y + 5), arrowprops=dict(arrowstyle='->', lw=1.2, color='#718096'))

# Stacking Classifier
draw_box(ax, 76, 4, 22, 20, 'STACKING ENSEMBLE', 'Base: Random Forest + XGBoost\nMeta: Logistic Regression\nAcc: 98.33% | AUC: 0.9989', '#C3DAFE', '#4C51BF', '#312E81')
ax.annotate('', xy=(87, 24), xytext=(87, 32), arrowprops=dict(arrowstyle='->', lw=2, color='#4C51BF'))

plt.savefig('presentation/assets_fake_news/fig1_system_architecture.png', dpi=300, bbox_inches='tight')
plt.close()
print('Generated fig1_system_architecture.png')

# 2. FIG 2: Data Flow Diagram (DFD Level 0 & 1)
fig, ax = plt.subplots(figsize=(12, 7), dpi=300)
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')

ax.text(50, 95, 'DATA FLOW DIAGRAM (DFD LEVEL 1): VERIFICATION PIPELINE', 
        ha='center', va='center', fontsize=14, fontweight='bold', color='#1A365D')

draw_box(ax, 4, 42, 16, 16, 'EXTERNAL ENTITY', 'End User / Newsroom\n(URL / Raw Text Input)', '#BEE3F8', '#3182CE', '#2A4365')
draw_box(ax, 24, 42, 16, 16, '1.0 INGEST & CLEAN', 'DOM Extraction\n& Lemmatization', '#EDF2F7', '#4A5568')
draw_box(ax, 44, 60, 18, 16, '2.1 STYLOMETRICS', 'TTR, FRE, Syllables,\nPunctuation Density', '#FEFCBF', '#D69E2E', '#744210')
draw_box(ax, 44, 24, 18, 16, '2.2 BIAS & FALLACY', 'S_idx, EHF, HUR, FSI,\nAllSides 2D Coords', '#FED7D7', '#E53E3E', '#9B2C2C')
draw_box(ax, 66, 42, 15, 16, '3.0 FUSED VECTOR', 'Concat 5,028 Dims\nStandard Scaling', '#E9D8FD', '#805AD5', '#553C9A')
draw_box(ax, 84, 42, 14, 16, '4.0 STACKING ML', 'RF + XGBoost\n-> Logistic Meta', '#C3DAFE', '#4C51BF', '#312E81')

ax.annotate('Article URL', xy=(24, 50), xytext=(20, 50), arrowprops=dict(arrowstyle='->', lw=1.5, color='#3182CE'))
ax.annotate('Clean Tokens', xy=(44, 68), xytext=(40, 54), arrowprops=dict(arrowstyle='->', lw=1.5, color='#4A5568'))
ax.annotate('Clean Tokens', xy=(44, 32), xytext=(40, 46), arrowprops=dict(arrowstyle='->', lw=1.5, color='#4A5568'))
ax.annotate('Dense Indices', xy=(66, 54), xytext=(62, 68), arrowprops=dict(arrowstyle='->', lw=1.5, color='#D69E2E'))
ax.annotate('Bias Vectors', xy=(66, 46), xytext=(62, 32), arrowprops=dict(arrowstyle='->', lw=1.5, color='#E53E3E'))
ax.annotate('X_fused', xy=(84, 50), xytext=(81, 50), arrowprops=dict(arrowstyle='->', lw=1.5, color='#805AD5'))

# Feedback
ax.annotate('Auditor Verdict & Explainability Heatmap', xy=(12, 42), xytext=(84, 20),
            arrowprops=dict(arrowstyle='->', lw=1.5, color='#38A169', connectionstyle='arc3,rad=-0.3'))

plt.savefig('presentation/assets_fake_news/fig2_data_flow_diagram.png', dpi=300, bbox_inches='tight')
plt.close()
print('Generated fig2_data_flow_diagram.png')

# 3. FIG 3: Stacking Ensemble Architecture
fig, ax = plt.subplots(figsize=(11, 7), dpi=300)
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')

ax.text(50, 95, 'CALIBRATED STACKING ENSEMBLE ARCHITECTURE', 
        ha='center', va='center', fontsize=14, fontweight='bold', color='#1A365D')

draw_box(ax, 5, 38, 20, 24, 'FUSED INPUT MATRIX', '5,028 Features\n(5,000 TF-IDF N-grams\n+ 28 Engineered Metrics)', '#E2E8F0', '#4A5568')

draw_box(ax, 34, 58, 24, 18, 'BASE LEARNER 1: RANDOM FOREST', '200 Decision Trees\nBalanced Subsample\nAcc: 97.08% | AUC: 0.9972', '#C6F6D5', '#38A169', '#22543D')
draw_box(ax, 34, 24, 24, 18, 'BASE LEARNER 2: XGBOOST', '150 Boosted Rounds (eta=0.08)\nHistogram Tree Method\nAcc: 97.92% | AUC: 0.9981', '#FEEBC8', '#DD6B20', '#7B341E')

draw_box(ax, 66, 38, 14, 24, 'BLENDED\nPROBABILITY\nSPACE', 'OOF Predictions\n[P_RF, P_XGB]\nCross-Validated', '#E9D8FD', '#805AD5', '#553C9A')

draw_box(ax, 84, 38, 14, 24, 'META-LEARNER\n(LOGISTIC REG)', 'L2 Regularized (C=1.0)\nOptimal Sigmoid Fit\nAcc: 98.33%\nAUC: 0.9989', '#C3DAFE', '#4C51BF', '#312E81')

ax.annotate('', xy=(34, 67), xytext=(25, 55), arrowprops=dict(arrowstyle='->', lw=1.5, color='#4A5568'))
ax.annotate('', xy=(34, 33), xytext=(25, 45), arrowprops=dict(arrowstyle='->', lw=1.5, color='#4A5568'))
ax.annotate('', xy=(66, 55), xytext=(58, 67), arrowprops=dict(arrowstyle='->', lw=1.5, color='#38A169'))
ax.annotate('', xy=(66, 45), xytext=(58, 33), arrowprops=dict(arrowstyle='->', lw=1.5, color='#DD6B20'))
ax.annotate('', xy=(84, 50), xytext=(80, 50), arrowprops=dict(arrowstyle='->', lw=1.5, color='#805AD5'))

plt.savefig('presentation/assets_fake_news/fig3_stacking_classifier.png', dpi=300, bbox_inches='tight')
plt.close()
print('Generated fig3_stacking_classifier.png')
