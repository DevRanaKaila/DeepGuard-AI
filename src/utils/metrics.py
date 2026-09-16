import numpy as np
from sklearn.metrics import roc_auc_score, f1_score, accuracy_score, roc_curve, confusion_matrix
import matplotlib.pyplot as plt

def compute_auc_roc(y_true, y_scores):
    try:
        return roc_auc_score(y_true, y_scores)
    except ValueError:
        return 0.5

def compute_f1_score(y_true, y_pred):
    return f1_score(y_true, y_pred, zero_division=0)

def compute_eer(y_true, y_scores):
    fpr, tpr, thresholds = roc_curve(y_true, y_scores)
    fnr = 1 - tpr
    idx = np.nanargmin(np.absolute((fnr - fpr)))
    return fpr[idx]

def compute_accuracy(y_true, y_pred):
    return accuracy_score(y_true, y_pred)

def compute_all_metrics(y_true, y_scores, threshold=0.5):
    y_pred = (np.array(y_scores) >= threshold).astype(int)
    y_true = np.array(y_true)
    
    return {
        'auc_roc': compute_auc_roc(y_true, y_scores),
        'f1_score': compute_f1_score(y_true, y_pred),
        'eer': compute_eer(y_true, y_scores),
        'accuracy': compute_accuracy(y_true, y_pred)
    }

def plot_roc_curve(y_true, y_scores, save_path=None):
    fpr, tpr, _ = roc_curve(y_true, y_scores)
    roc_auc = compute_auc_roc(y_true, y_scores)
    
    fig, ax = plt.subplots()
    ax.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (area = {roc_auc:.2f})')
    ax.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    ax.set_xlim([0.0, 1.0])
    ax.set_ylim([0.0, 1.05])
    ax.set_xlabel('False Positive Rate')
    ax.set_ylabel('True Positive Rate')
    ax.set_title('Receiver Operating Characteristic')
    ax.legend(loc="lower right")
    
    if save_path:
        fig.savefig(save_path)
    return fig

def plot_confusion_matrix(y_true, y_pred, save_path=None):
    cm = confusion_matrix(y_true, y_pred)
    fig, ax = plt.subplots()
    cax = ax.matshow(cm, cmap=plt.cm.Blues)
    fig.colorbar(cax)
    
    for (i, j), val in np.ndenumerate(cm):
        ax.text(j, i, f'{val}', ha='center', va='center')
        
    ax.set_xlabel('Predicted labels')
    ax.set_ylabel('True labels')
    ax.set_title('Confusion Matrix')
    
    if save_path:
        fig.savefig(save_path)
    return fig

class MetricTracker:
    def __init__(self):
        self.reset()
        
    def reset(self):
        self.val = 0
        self.avg = 0
        self.sum = 0
        self.count = 0
        
    def update(self, val, n=1):
        self.val = val
        self.sum += val * n
        self.count += n
        self.avg = self.sum / self.count
