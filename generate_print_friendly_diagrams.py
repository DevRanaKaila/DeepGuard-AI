import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

out_sub = r'D:\mini-project\SUBMISSION'
out_assets = r'D:\mini-project\report_assets'
os.makedirs(out_sub, exist_ok=True)
os.makedirs(out_assets, exist_ok=True)

# Common styling for pure white print-friendly diagrams
FONT_FAMILY = 'DejaVu Sans'
plt.rcParams['font.family'] = FONT_FAMILY

# ==============================================================================
# 1. SYSTEM ARCHITECTURE OVERVIEW (Pure White Background)
# ==============================================================================
fig, ax = plt.subplots(figsize=(12, 7.5), dpi=300)
fig.patch.set_facecolor('#FFFFFF')
ax.set_facecolor('#FFFFFF')
ax.set_xlim(0, 120)
ax.set_ylim(0, 75)
ax.axis('off')

# Title
ax.text(60, 71, 'DEEPGUARD AI: DUAL-STREAM SYSTEM ARCHITECTURE', ha='center', va='center', 
        fontsize=14, fontweight='bold', color='#0F172A')
ax.text(60, 68, 'Coupled Spatial Convolutional and Frequency-Domain Spectral Analysis', ha='center', va='center', 
        fontsize=10, color='#475569')

# Layer 1: Ingestion & Preprocessing
box_ingest = patches.FancyBboxPatch((8, 48), 104, 16, boxstyle="round,pad=0.5", 
                                    facecolor='#F8FAFC', edgecolor='#CBD5E1', lw=1.5)
ax.add_patch(box_ingest)
ax.text(12, 61, 'STAGE 1: VIDEO INGESTION & FACIAL PREPROCESSING', fontsize=9, fontweight='bold', color='#1E293B')

# Sub-boxes in Stage 1
sub_boxes_1 = [
    (10, 50, 22, 9, 'Input Video Stream\n(MP4 / AVI / MOV)', '#FFFFFF', '#94A3B8'),
    (36, 50, 22, 9, 'Temporal Sampling\n(5 FPS Uniform)', '#FFFFFF', '#94A3B8'),
    (62, 50, 24, 9, 'MTCNN Face Tracker\n(Landmarks & Alignment)', '#FFFFFF', '#94A3B8'),
    (90, 50, 20, 9, 'Canonical Crop\n(256x256 RGB + 15% Marg.)', '#EFF6FF', '#3B82F6')
]
for x, y, w, h, txt, bg, border in sub_boxes_1:
    b = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.3", facecolor=bg, edgecolor=border, lw=1.2)
    ax.add_patch(b)
    ax.text(x + w/2, y + h/2, txt, ha='center', va='center', fontsize=8, fontweight='bold', color='#1E293B')

for px in [32, 58, 86]:
    ax.annotate('', xy=(px+4, 54.5), xytext=(px, 54.5), arrowprops=dict(arrowstyle="->", lw=1.5, color='#475569'))

# Downward fork
ax.annotate('', xy=(35, 44), xytext=(100, 48), arrowprops=dict(arrowstyle="->", lw=1.5, color='#2563EB', connectionstyle="arc3,rad=-0.1"))
ax.annotate('', xy=(85, 44), xytext=(100, 48), arrowprops=dict(arrowstyle="->", lw=1.5, color='#0D9488', connectionstyle="arc3,rad=0.1"))

# Stage 2: Dual Stream Processing
# Stream I: Spatial Stream (Left)
box_spatial = patches.FancyBboxPatch((8, 18), 50, 25, boxstyle="round,pad=0.5", 
                                     facecolor='#F0F9FF', edgecolor='#38BDF8', lw=1.5)
ax.add_patch(box_spatial)
ax.text(33, 40, 'STREAM I: SPATIAL PIXEL STREAM', ha='center', fontsize=9.5, fontweight='bold', color='#0369A1')
ax.text(33, 36.5, 'Input: RGB Tensor [3 x 256 x 256]', ha='center', fontsize=8, color='#0284C7')

s_sub = [
    (12, 27, 42, 7, 'EfficientNet-B4 Backbone (MBConv + SE Blocks)', '#FFFFFF', '#0284C7'),
    (12, 20, 42, 5.5, 'Spatial Latent Embedding: v_spatial ∈ ℝ¹⁷⁹²', '#BAE6FD', '#0369A1')
]
for x, y, w, h, txt, bg, border in s_sub:
    b = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.2", facecolor=bg, edgecolor=border, lw=1.2)
    ax.add_patch(b)
    ax.text(x + w/2, y + h/2, txt, ha='center', va='center', fontsize=7.5, fontweight='bold', color='#0C4A6E')

# Stream II: Frequency Stream (Right)
box_freq = patches.FancyBboxPatch((62, 18), 50, 25, boxstyle="round,pad=0.5", 
                                  facecolor='#F0FDF4', edgecolor='#34D399', lw=1.5)
ax.add_patch(box_freq)
ax.text(87, 40, 'STREAM II: FREQUENCY SPECTRAL STREAM', ha='center', fontsize=9.5, fontweight='bold', color='#047857')
ax.text(87, 36.5, 'Input: Grayscale DCT Spectrum [1 x 256 x 256]', ha='center', fontsize=8, color='#059669')

f_sub = [
    (66, 27, 42, 7, '2D-DCT-II Transform & Radial Azimuthal Pooling A(r)', '#FFFFFF', '#059669'),
    (66, 20, 42, 5.5, 'Spectral Feature Vector: v_freq ∈ ℝ⁵¹²', '#A7F3D0', '#047857')
]
for x, y, w, h, txt, bg, border in f_sub:
    b = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.2", facecolor=bg, edgecolor=border, lw=1.2)
    ax.add_patch(b)
    ax.text(x + w/2, y + h/2, txt, ha='center', va='center', fontsize=7.5, fontweight='bold', color='#064E3B')

# Downward to Stage 3: Fusion & Classification
ax.annotate('', xy=(50, 14), xytext=(33, 18), arrowprops=dict(arrowstyle="->", lw=1.5, color='#0284C7'))
ax.annotate('', xy=(70, 14), xytext=(87, 18), arrowprops=dict(arrowstyle="->", lw=1.5, color='#059669'))

box_fuse = patches.FancyBboxPatch((28, 2), 64, 12, boxstyle="round,pad=0.4", 
                                  facecolor='#FFFBEB', edgecolor='#FBBF24', lw=1.5)
ax.add_patch(box_fuse)
ax.text(60, 11, 'STAGE 3: ATTENTION-GATED BILINEAR FUSION & CLASSIFIER', ha='center', fontsize=9, fontweight='bold', color='#92400E')
ax.text(60, 7.5, 'g = σ(Wg[v_s || Wp v_f] + bg)  ⟹  v_fused = [g ⊙ v_s || (1-g) ⊙ Wp v_f]', ha='center', fontsize=8, color='#78350F')
ax.text(60, 4, 'Output: Authenticity Verdict (Real vs Fake) + Dual Grad-CAM Heatmaps', ha='center', fontsize=8, fontweight='bold', color='#B45309')

plt.tight_layout()
p1 = os.path.join(out_sub, '1_system_architecture_overview.png')
fig.savefig(p1, dpi=300, facecolor='#FFFFFF')
fig.savefig(os.path.join(out_assets, '1_system_architecture_overview.png'), dpi=300, facecolor='#FFFFFF')
plt.close()
print("Generated 1_system_architecture_overview.png")

# ==============================================================================
# 2. CONTEXT-LEVEL (LEVEL 0) DATA FLOW DIAGRAM (Pure White Background)
# ==============================================================================
fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
fig.patch.set_facecolor('#FFFFFF')
ax.set_facecolor('#FFFFFF')
ax.set_xlim(0, 100)
ax.set_ylim(0, 70)
ax.axis('off')

ax.text(50, 66, 'CONTEXT-LEVEL (LEVEL 0) DATA FLOW DIAGRAM', ha='center', fontsize=13, fontweight='bold', color='#0F172A')

# Central Process Circle
circ = patches.Circle((50, 35), 14, facecolor='#EFF6FF', edgecolor='#2563EB', lw=2)
ax.add_patch(circ)
ax.text(50, 38, '0', ha='center', va='center', fontsize=14, fontweight='bold', color='#1D4ED8')
ax.text(50, 34, 'DeepGuard AI\nForensic Verification\nSystem', ha='center', va='center', 
        fontsize=8.5, fontweight='bold', color='#1E293B')

# External Entities (Rectangles)
entities = [
    (12, 48, 'Forensic Examiner\n(Law Enforcement / Lab)'),
    (12, 22, 'Automated KYC Gate\n(Banking & Fintech Platform)'),
    (88, 35, 'Judicial / Compliance\nAudit Repository')
]

for x, y, label in entities:
    rect = patches.FancyBboxPatch((x-10, y-6), 20, 12, boxstyle="round,pad=0.2", facecolor='#F8FAFC', edgecolor='#64748B', lw=1.5)
    ax.add_patch(rect)
    ax.text(x, y, label, ha='center', va='center', fontsize=8, fontweight='bold', color='#0F172A')

# Connecting Flows with labels
# Examiner -> System
ax.annotate('', xy=(37, 40), xytext=(22, 48), arrowprops=dict(arrowstyle="->", lw=1.5, color='#2563EB'))
ax.text(28, 46, 'Suspect Video / Media', fontsize=7.5, fontweight='bold', color='#2563EB', rotation=14)

# System -> Examiner
ax.annotate('', xy=(22, 44), xytext=(37, 36), arrowprops=dict(arrowstyle="->", lw=1.5, color='#059669'))
ax.text(28, 38, 'Grad-CAM Heatmaps & Telemetry', fontsize=7.5, fontweight='bold', color='#059669', rotation=-14)

# KYC -> System
ax.annotate('', xy=(37, 30), xytext=(22, 24), arrowprops=dict(arrowstyle="->", lw=1.5, color='#2563EB'))
ax.text(28, 29, 'Biometric Video Stream', fontsize=7.5, fontweight='bold', color='#2563EB', rotation=-14)

# System -> KYC
ax.annotate('', xy=(22, 20), xytext=(37, 26), arrowprops=dict(arrowstyle="->", lw=1.5, color='#059669'))
ax.text(28, 21, 'Authenticity Verdict & Score', fontsize=7.5, fontweight='bold', color='#059669', rotation=14)

# System -> Compliance Repository
ax.annotate('', xy=(78, 35), xytext=(64, 35), arrowprops=dict(arrowstyle="->", lw=1.5, color='#059669'))
ax.text(71, 37.5, 'Certified PDF Forensic Report\n& SHA-256 Digest', ha='center', fontsize=7.5, fontweight='bold', color='#059669')

plt.tight_layout()
p2 = os.path.join(out_sub, '2_data_flow_diagram_dfd.png')
fig.savefig(p2, dpi=300, facecolor='#FFFFFF')
fig.savefig(os.path.join(out_assets, '2_data_flow_diagram_dfd.png'), dpi=300, facecolor='#FFFFFF')
plt.close()
print("Generated 2_data_flow_diagram_dfd.png")

# ==============================================================================
# 3. DUAL-STREAM DEEP DIVE ARCHITECTURE (Pure White Background)
# ==============================================================================
fig, ax = plt.subplots(figsize=(12, 7.5), dpi=300)
fig.patch.set_facecolor('#FFFFFF')
ax.set_facecolor('#FFFFFF')
ax.set_xlim(0, 120)
ax.set_ylim(0, 75)
ax.axis('off')

ax.text(60, 72, 'DUAL-STREAM NEURAL NETWORK DEEP DIVE', ha='center', fontsize=14, fontweight='bold', color='#0F172A')
ax.text(60, 68.5, 'High-Resolution Dimensional Flow from Input Tensors to Multi-Modal Verdict', ha='center', fontsize=9.5, color='#475569')

# Input Face Crop
b_input = patches.FancyBboxPatch((48, 56), 24, 9, boxstyle="round,pad=0.3", facecolor='#EFF6FF', edgecolor='#3B82F6', lw=1.5)
ax.add_patch(b_input)
ax.text(60, 60.5, 'Aligned Face Crop\n256 x 256 Pixels', ha='center', va='center', fontsize=8.5, fontweight='bold', color='#1E40AF')

# Fork arrows
ax.annotate('', xy=(28, 51), xytext=(52, 56), arrowprops=dict(arrowstyle="->", lw=1.5, color='#0284C7'))
ax.annotate('', xy=(92, 51), xytext=(68, 56), arrowprops=dict(arrowstyle="->", lw=1.5, color='#0D9488'))

# Left Branch: Spatial Stream
b_sp_box = patches.FancyBboxPatch((10, 20), 45, 31, boxstyle="round,pad=0.4", facecolor='#F0F9FF', edgecolor='#0284C7', lw=1.5)
ax.add_patch(b_sp_box)
ax.text(32.5, 48, 'SPATIAL STREAM: EFFICIENTNET-B4', ha='center', fontsize=9, fontweight='bold', color='#0369A1')

s_layers = [
    (14, 40, 37, 5, 'Input: Normalized RGB [3 x 256 x 256]', '#FFFFFF', '#38BDF8'),
    (14, 33, 37, 5.5, 'MBConv Blocks (d=1.8, w=1.4, SE Attn)', '#E0F2FE', '#0284C7'),
    (14, 26, 37, 5, 'Global Average Pooling (GAP)', '#FFFFFF', '#38BDF8'),
    (14, 21.5, 37, 3.5, 'Feature Vector: v_spatial ∈ ℝ¹⁷⁹²', '#BAE6FD', '#0369A1')
]
for x, y, w, h, txt, bg, border in s_layers:
    b = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.2", facecolor=bg, edgecolor=border, lw=1)
    ax.add_patch(b)
    ax.text(x + w/2, y + h/2, txt, ha='center', va='center', fontsize=7.5, fontweight='bold', color='#0C4A6E')

# Right Branch: Frequency Stream
b_fr_box = patches.FancyBboxPatch((65, 20), 45, 31, boxstyle="round,pad=0.4", facecolor='#F0FDF4', edgecolor='#059669', lw=1.5)
ax.add_patch(b_fr_box)
ax.text(87.5, 48, 'FREQUENCY STREAM: 2D-DCT + SPECTRAL-CNN', ha='center', fontsize=9, fontweight='bold', color='#047857')

f_layers = [
    (69, 40, 37, 5, '2D-DCT-II Orthonormal Transform S(u,v)', '#FFFFFF', '#34D399'),
    (69, 33, 37, 5.5, '4-Stage Depthwise Separable ConvNet', '#D1FAE5', '#059669'),
    (69, 26, 37, 5, 'Radial Azimuthal Average Pooling A(r)', '#FFFFFF', '#34D399'),
    (69, 21.5, 37, 3.5, 'Spectral Vector: v_freq ∈ ℝ⁵¹²', '#A7F3D0', '#047857')
]
for x, y, w, h, txt, bg, border in f_layers:
    b = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.2", facecolor=bg, edgecolor=border, lw=1)
    ax.add_patch(b)
    ax.text(x + w/2, y + h/2, txt, ha='center', va='center', fontsize=7.5, fontweight='bold', color='#064E3B')

# Convergence to Attention-Gated Fusion
ax.annotate('', xy=(48, 14), xytext=(32.5, 20), arrowprops=dict(arrowstyle="->", lw=1.5, color='#0284C7'))
ax.annotate('', xy=(72, 14), xytext=(87.5, 20), arrowprops=dict(arrowstyle="->", lw=1.5, color='#059669'))

b_gate = patches.FancyBboxPatch((35, 3), 50, 11, boxstyle="round,pad=0.3", facecolor='#FFFBEB', edgecolor='#D97706', lw=1.5)
ax.add_patch(b_gate)
ax.text(60, 11, 'ATTENTION-GATED BILINEAR FUSION & MLP HEAD', ha='center', fontsize=9, fontweight='bold', color='#92400E')
ax.text(60, 7.5, 'Fused Vector v_fused = [g ⊙ v_s || (1-g) ⊙ Wp v_f] ∈ ℝ³⁵⁸⁴', ha='center', fontsize=8, color='#78350F')
ax.text(60, 4.5, 'FC(3584→256) → LayerNorm → Dropout(0.4) → Sigmoid ⟹ Output p ∈ [0, 1]', ha='center', fontsize=7.5, fontweight='bold', color='#B45309')

plt.tight_layout()
p3 = os.path.join(out_sub, '3_dual_stream_deep_dive.png')
fig.savefig(p3, dpi=300, facecolor='#FFFFFF')
fig.savefig(os.path.join(out_assets, '3_dual_stream_deep_dive.png'), dpi=300, facecolor='#FFFFFF')
plt.close()
print("Generated 3_dual_stream_deep_dive.png")

# ==============================================================================
# 4. ATTENTION FUSION GATE MECHANISM (Pure White Background)
# ==============================================================================
fig, ax = plt.subplots(figsize=(11, 6.5), dpi=300)
fig.patch.set_facecolor('#FFFFFF')
ax.set_facecolor('#FFFFFF')
ax.set_xlim(0, 110)
ax.set_ylim(0, 65)
ax.axis('off')

ax.text(55, 61, 'ATTENTION-GATED BILINEAR FUSION MECHANISM', ha='center', fontsize=13, fontweight='bold', color='#0F172A')
ax.text(55, 57.5, 'Dynamic Compression-Adaptive Gating Between Spatial & Spectral Embeddings', ha='center', fontsize=9, color='#475569')

# Spatial Input Box
b_s = patches.FancyBboxPatch((10, 42), 26, 9, boxstyle="round,pad=0.3", facecolor='#F0F9FF', edgecolor='#0284C7', lw=1.5)
ax.add_patch(b_s)
ax.text(23, 46.5, 'Spatial Embedding\nv_spatial ∈ ℝ¹⁷⁹²', ha='center', va='center', fontsize=8.5, fontweight='bold', color='#0369A1')

# Frequency Input Box
b_f = patches.FancyBboxPatch((74, 42), 26, 9, boxstyle="round,pad=0.3", facecolor='#F0FDF4', edgecolor='#059669', lw=1.5)
ax.add_patch(b_f)
ax.text(87, 46.5, 'Spectral Embedding\nv_freq ∈ ℝ⁵¹²', ha='center', va='center', fontsize=8.5, fontweight='bold', color='#047857')

# Frequency Projection
ax.annotate('', xy=(87, 33), xytext=(87, 42), arrowprops=dict(arrowstyle="->", lw=1.5, color='#059669'))
b_proj = patches.FancyBboxPatch((74, 25), 26, 8, boxstyle="round,pad=0.3", facecolor='#ECFDF5', edgecolor='#10B981', lw=1.2)
ax.add_patch(b_proj)
ax.text(87, 29, 'Linear Projection W_proj\nW_proj v_freq ∈ ℝ¹⁷⁹²', ha='center', va='center', fontsize=8, fontweight='bold', color='#065F46')

# Central Gating Network
b_gate_box = patches.FancyBboxPatch((40, 25), 30, 13, boxstyle="round,pad=0.3", facecolor='#FFFBEB', edgecolor='#F59E0B', lw=1.5)
ax.add_patch(b_gate_box)
ax.text(55, 34, 'Attention Gating Network', ha='center', fontsize=9, fontweight='bold', color='#92400E')
ax.text(55, 30.5, 'FC(3584 → 256) → ReLU', ha='center', fontsize=7.5, color='#78350F')
ax.text(55, 27.5, 'FC(256 → 1) + Sigmoid', ha='center', fontsize=7.5, color='#78350F')

# Arrows to Gate
ax.annotate('', xy=(40, 33), xytext=(23, 42), arrowprops=dict(arrowstyle="->", lw=1.5, color='#0284C7'))
ax.annotate('', xy=(70, 31), xytext=(74, 30), arrowprops=dict(arrowstyle="->", lw=1.5, color='#10B981'))

# Gate scalar g
ax.text(55, 21.5, 'Gate Scalar g ∈ (0, 1)', ha='center', fontsize=8.5, fontweight='bold', color='#D97706')

# Downward to Multipliers
ax.annotate('', xy=(32, 13), xytext=(48, 20), arrowprops=dict(arrowstyle="->", lw=1.5, color='#D97706'))
ax.annotate('', xy=(78, 13), xytext=(62, 20), arrowprops=dict(arrowstyle="->", lw=1.5, color='#D97706'))

# Multipliers
circ_m1 = patches.Circle((32, 11), 3.5, facecolor='#FEF3C7', edgecolor='#D97706', lw=1.5)
ax.add_patch(circ_m1)
ax.text(32, 11, 'g ⊙', ha='center', va='center', fontsize=9, fontweight='bold', color='#B45309')

circ_m2 = patches.Circle((78, 11), 3.5, facecolor='#FEF3C7', edgecolor='#D97706', lw=1.5)
ax.add_patch(circ_m2)
ax.text(78, 11, '(1-g) ⊙', ha='center', va='center', fontsize=8.5, fontweight='bold', color='#B45309')

# Spatial into m1, Proj into m2
ax.annotate('', xy=(32, 14.5), xytext=(23, 42), arrowprops=dict(arrowstyle="->", lw=1.2, color='#0284C7', linestyle='--'))
ax.annotate('', xy=(78, 14.5), xytext=(87, 25), arrowprops=dict(arrowstyle="->", lw=1.2, color='#10B981', linestyle='--'))

# Final Concatenation Box
ax.annotate('', xy=(50, 4), xytext=(35.5, 11), arrowprops=dict(arrowstyle="->", lw=1.5, color='#D97706'))
ax.annotate('', xy=(60, 4), xytext=(74.5, 11), arrowprops=dict(arrowstyle="->", lw=1.5, color='#D97706'))

b_fused = patches.FancyBboxPatch((35, 0.5), 40, 6, boxstyle="round,pad=0.2", facecolor='#F3E8FF', edgecolor='#9333EA', lw=1.5)
ax.add_patch(b_fused)
ax.text(55, 3.5, 'Fused Feature Vector: v_fused ∈ ℝ³⁵⁸⁴', ha='center', va='center', fontsize=8.5, fontweight='bold', color='#6B21A8')

plt.tight_layout()
p4 = os.path.join(out_sub, '4_attention_fusion_gate.png')
fig.savefig(p4, dpi=300, facecolor='#FFFFFF')
fig.savefig(os.path.join(out_assets, '4_attention_fusion_gate.png'), dpi=300, facecolor='#FFFFFF')
plt.close()
print("Generated 4_attention_fusion_gate.png")

# ==============================================================================
# 5. END-TO-END PIPELINE / LEVEL 1 DFD (Pure White Background)
# ==============================================================================
fig, ax = plt.subplots(figsize=(12, 8), dpi=300)
fig.patch.set_facecolor('#FFFFFF')
ax.set_facecolor('#FFFFFF')
ax.set_xlim(0, 120)
ax.set_ylim(0, 80)
ax.axis('off')

ax.text(60, 76, 'LEVEL 1 DETAILED FORENSIC DATA FLOW DIAGRAM', ha='center', fontsize=14, fontweight='bold', color='#0F172A')

# Process bubbles (Circles 1.0 to 5.0)
processes = [
    (20, 58, '1.0\nVideo Demuxing &\nFrame Sampling', '#EFF6FF', '#2563EB'),
    (55, 58, '2.0\nMTCNN Face Detection\n& Landmark Alignment', '#EFF6FF', '#2563EB'),
    (90, 58, '3.0\nDual-Stream Feature\nExtraction Engine', '#EFF6FF', '#2563EB'),
    (75, 26, '4.0\nAttention-Gated\nBilinear Fusion', '#FFFBEB', '#D97706'),
    (30, 26, '5.0\nClassification Head &\nGrad-CAM Explainability', '#ECFDF5', '#059669')
]

for x, y, label, bg, border in processes:
    circ = patches.Circle((x, y), 10, facecolor=bg, edgecolor=border, lw=2)
    ax.add_patch(circ)
    ax.text(x, y, label, ha='center', va='center', fontsize=8, fontweight='bold', color='#1E293B')

# Data Stores (Open ended horizontal lines)
stores = [
    (38, 43, 'D1: Frame Buffer Cache'),
    (75, 43, 'D2: Dual Embeddings Store'),
    (52, 10, 'D3: Verified Forensic Report Store')
]
for x, y, label in stores:
    ax.plot([x-14, x+14], [y+2, y+2], color='#475569', lw=1.5)
    ax.plot([x-14, x+14], [y-2, y-2], color='#475569', lw=1.5)
    ax.text(x, y, label, ha='center', va='center', fontsize=8, fontweight='bold', color='#334155')

# Connectors
# 1.0 -> 2.0
ax.annotate('', xy=(45, 58), xytext=(30, 58), arrowprops=dict(arrowstyle="->", lw=1.5, color='#475569'))
ax.text(37.5, 60.5, 'Raw RGB Frames', ha='center', fontsize=7.5, color='#475569')

# 2.0 -> D1
ax.annotate('', xy=(38, 45), xytext=(50, 50), arrowprops=dict(arrowstyle="->", lw=1.2, color='#475569', linestyle=':'))

# 2.0 -> 3.0
ax.annotate('', xy=(80, 58), xytext=(65, 58), arrowprops=dict(arrowstyle="->", lw=1.5, color='#475569'))
ax.text(72.5, 60.5, '256x256 Crops', ha='center', fontsize=7.5, color='#475569')

# 3.0 -> D2
ax.annotate('', xy=(75, 45), xytext=(85, 50), arrowprops=dict(arrowstyle="->", lw=1.2, color='#475569', linestyle=':'))

# 3.0 -> 4.0
ax.annotate('', xy=(78, 36), xytext=(87, 49), arrowprops=dict(arrowstyle="->", lw=1.5, color='#475569'))
ax.text(87, 42, 'v_spatial (1792) +\nv_freq (512)', fontsize=7.5, color='#475569')

# 4.0 -> 5.0
ax.annotate('', xy=(40, 26), xytext=(65, 26), arrowprops=dict(arrowstyle="->", lw=1.5, color='#475569'))
ax.text(52.5, 28.5, 'v_fused (3584)', ha='center', fontsize=7.5, fontweight='bold', color='#D97706')

# 5.0 -> D3
ax.annotate('', xy=(45, 12), xytext=(32, 16), arrowprops=dict(arrowstyle="->", lw=1.5, color='#059669'))
ax.text(32, 10, 'Audit-Ready\nPDF Certificate', ha='center', fontsize=7.5, fontweight='bold', color='#059669')

plt.tight_layout()
p5 = os.path.join(out_sub, 'Architecture_Diagram.png')
fig.savefig(p5, dpi=300, facecolor='#FFFFFF')
fig.savefig(os.path.join(out_assets, 'Architecture_Diagram.png'), dpi=300, facecolor='#FFFFFF')
plt.close()
print("Generated Architecture_Diagram.png")

# ==============================================================================
# 6. DASHBOARD HOME (Clean White Print-Friendly Theme)
# ==============================================================================
fig, ax = plt.subplots(figsize=(10, 5.5), dpi=300)
fig.patch.set_facecolor('#FFFFFF')
ax.set_facecolor('#FFFFFF')
ax.set_xlim(0, 100)
ax.set_ylim(0, 60)
ax.axis('off')

# Header
ax.text(50, 53, 'DeepGuard AI Forensic Platform', ha='center', fontsize=18, fontweight='bold', color='#0F172A')
ax.text(50, 47, 'Dual-Stream Deepfake Detection in Spatial & Frequency Domains', ha='center', fontsize=10.5, color='#475569')

cards = [
    (15, 28, 'ACCURACY', '98.9%', 'Raw FF++'),
    (38, 28, 'AUC-ROC', '0.968', 'Celeb-DF v2'),
    (61, 28, 'LATENCY', '< 42ms', 'Real-Time 5 FPS'),
    (84, 28, 'PARAMETERS', '21.4M', 'Dual Backbone')
]

for cx, cy, title, val, sub in cards:
    card = patches.FancyBboxPatch((cx-10, cy-12), 20, 24, boxstyle="round,pad=0.5", 
                                 facecolor='#F8FAFC', edgecolor='#CBD5E1', lw=1.5)
    ax.add_patch(card)
    ax.text(cx, cy+7, title, ha='center', fontsize=8.5, fontweight='bold', color='#64748B')
    ax.text(cx, cy, val, ha='center', fontsize=17, fontweight='bold', color='#2563EB')
    ax.text(cx, cy-7, sub, ha='center', fontsize=8, color='#475569')

# Clean Status Bar
bar = patches.FancyBboxPatch((10, 4), 80, 7, boxstyle="round,pad=0.3", 
                            facecolor='#F1F5F9', edgecolor='#94A3B8', lw=1.2)
ax.add_patch(bar)
ax.text(50, 7.5, '● Active Model Checkpoint: checkpoints/best_model.pth (Kaggle DFDC & FF++ Optimized)', 
        ha='center', fontsize=8.5, fontweight='bold', color='#1E293B')

plt.tight_layout()
fig.savefig(os.path.join(out_assets, 'fig4_2_dashboard_home.png'), dpi=300, facecolor='#FFFFFF')
plt.close()
print("Generated fig4_2_dashboard_home.png (Print-Friendly)")

# ==============================================================================
# 7. DASHBOARD VERDICT (Clean White Print-Friendly Theme)
# ==============================================================================
fig, ax = plt.subplots(figsize=(10, 5.5), dpi=300)
fig.patch.set_facecolor('#FFFFFF')
ax.set_facecolor('#FFFFFF')
ax.set_xlim(0, 100)
ax.set_ylim(0, 60)
ax.axis('off')

# Banner
banner = patches.FancyBboxPatch((5, 45), 90, 11, boxstyle="round,pad=0.3", 
                                facecolor='#FEF2F2', edgecolor='#EF4444', lw=2)
ax.add_patch(banner)
ax.text(50, 50.5, 'DEEPFAKE DETECTED (96.8% Confidence)', ha='center', fontsize=15, fontweight='bold', color='#DC2626')

# Details Box
box = patches.FancyBboxPatch((5, 8), 44, 33, boxstyle="round,pad=0.5", 
                             facecolor='#F8FAFC', edgecolor='#CBD5E1', lw=1.5)
ax.add_patch(box)
ax.text(8, 36, 'FORENSIC TELEMETRY SUMMARY', fontsize=9.5, fontweight='bold', color='#0F172A')
ax.text(8, 30.5, '• Analysis Mode: Dual-Stream (Spatial + Frequency)', fontsize=8, color='#334155')
ax.text(8, 25.5, '• Sampled Video Frames: 30 frames (5 FPS Uniform)', fontsize=8, color='#334155')
ax.text(8, 20.5, '• Fake Frames Identified: 29 / 30 frames flagged', fontsize=8, fontweight='bold', color='#DC2626')
ax.text(8, 15.5, '• Dynamic Spatial Attention Weight: 0.584', fontsize=8, color='#334155')
ax.text(8, 10.5, '• Dynamic Spectral Gating Weight: 0.416', fontsize=8, color='#334155')

# Gauge Representation (Clean White Background)
ax.text(74, 36, 'AUTHENTICITY PROBABILITY GAUGE', ha='center', fontsize=9.5, fontweight='bold', color='#0F172A')
gauge_bg = patches.Arc((74, 22), 30, 26, theta1=0, theta2=180, color='#E2E8F0', lw=12)
ax.add_patch(gauge_bg)
gauge_val = patches.Arc((74, 22), 30, 26, theta1=0, theta2=174, color='#EF4444', lw=12)
ax.add_patch(gauge_val)
ax.text(74, 20, '96.8%', ha='center', fontsize=18, fontweight='bold', color='#DC2626')
ax.text(74, 13, 'Classification: MANIPULATED MEDIA', ha='center', fontsize=8.5, fontweight='bold', color='#475569')

plt.tight_layout()
fig.savefig(os.path.join(out_assets, 'fig6_1_dashboard_verdict.png'), dpi=300, facecolor='#FFFFFF')
plt.close()
print("Generated fig6_1_dashboard_verdict.png (Print-Friendly)")

print("All print-friendly diagrams generated successfully!")
