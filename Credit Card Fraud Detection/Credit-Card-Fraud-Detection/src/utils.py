import json
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report, roc_curve, roc_auc_score, confusion_matrix

def save_json(obj, path):
    with open(path, "w") as f:
        json.dump(obj, f, indent=2)

def plot_confusion(cm, labels, path):
    import numpy as np
    fig = plt.figure(figsize=(4,4))
    plt.imshow(cm, interpolation='nearest')
    plt.title('Confusion Matrix')
    plt.xticks([0,1], labels)
    plt.yticks([0,1], labels)
    plt.colorbar()
    thresh = cm.max() / 2.
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            plt.text(j, i, format(cm[i, j], 'd'),
                     ha="center", va="center",
                     color="white" if cm[i, j] > thresh else "black")
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.tight_layout()
    fig.savefig(path, dpi=160)
    plt.close(fig)

def plot_roc(y_true, y_prob, path):
    fpr, tpr, _ = roc_curve(y_true, y_prob)
    auc = roc_auc_score(y_true, y_prob)
    fig = plt.figure(figsize=(4,4))
    plt.plot(fpr, tpr, label=f'ROC AUC = {auc:.3f}')
    plt.plot([0,1],[0,1],'--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curve')
    plt.legend(loc='lower right')
    plt.tight_layout()
    fig.savefig(path, dpi=160)
    plt.close(fig)

def summarize_metrics(y_true, y_pred, y_prob):
    report = classification_report(y_true, y_pred, output_dict=True, zero_division=0)
    from sklearn.metrics import roc_auc_score
    roc_auc = roc_auc_score(y_true, y_prob)
    return {
        "precision": report["1"]["precision"],
        "recall": report["1"]["recall"],
        "f1": report["1"]["f1-score"],
        "roc_auc": roc_auc,
        "support_fraud": int(report["1"]["support"])
    }