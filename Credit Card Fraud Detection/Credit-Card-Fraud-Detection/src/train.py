import argparse, os, pandas as pd, numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.compose import ColumnTransformer
from sklearn.metrics import confusion_matrix
from imblearn.pipeline import Pipeline as ImbPipeline
from joblib import dump

from utils import summarize_metrics, save_json, plot_confusion, plot_roc

def load_data(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Dataset not found at {path}. Please place creditcard.csv under data/.")
    df = pd.read_csv(path)
    if "Class" not in df.columns:
        raise ValueError("Target column 'Class' not found.")
    return df

def build_splits(df, test_size=0.2, seed=42):
    y = df["Class"].astype(int)
    X = df.drop(columns=["Class"])
    num_cols = X.columns.tolist()
    X_tr, X_va, y_tr, y_va = train_test_split(X, y, test_size=test_size, random_state=seed, stratify=y)
    return X_tr, X_va, y_tr, y_va, num_cols

def make_pipeline(model, num_cols):
    pre = ColumnTransformer([("num", StandardScaler(with_mean=False), num_cols)], remainder="drop")
    if model == "lr":
        clf = LogisticRegression(max_iter=2000, class_weight="balanced")
    elif model == "rf":
        clf = RandomForestClassifier(n_estimators=300, class_weight="balanced_subsample", n_jobs=-1, random_state=42)
    else:
        raise ValueError("Choose model from: lr, rf")
    return ImbPipeline([("pre", pre), ("clf", clf)])

def main(args):
    os.makedirs("models", exist_ok=True)
    df = load_data(args.data)
    X_tr, X_va, y_tr, y_va, num_cols = build_splits(df, args.test_size, args.seed)
    pipe = make_pipeline(args.model, num_cols)
    pipe.fit(X_tr, y_tr)

    y_pred = pipe.predict(X_va)
    if hasattr(pipe, "predict_proba"):
        y_prob = pipe.predict_proba(X_va)[:,1]
    else:
        y_prob = y_pred.astype(float)

    metrics = summarize_metrics(y_va, y_pred, y_prob)
    cm = confusion_matrix(y_va, y_pred, labels=[0,1])
    plot_confusion(cm, ["Legit","Fraud"], os.path.join("models", f"confusion_{args.model}.png"))
    plot_roc(y_va, y_prob, os.path.join("models", f"roc_{args.model}.png"))

    dump(pipe, os.path.join("models", f"model_{args.model}.pkl"))
    save_json(metrics, os.path.join("models", f"report_{args.model}.json"))

    print("=== Validation Metrics (fraud class) ===")
    for k,v in metrics.items():
        print(f"{k}: {v}")

if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--data", type=str, default="data/creditcard.csv")
    p.add_argument("--model", type=str, default="lr", choices=["lr","rf"])
    p.add_argument("--test_size", type=float, default=0.2)
    p.add_argument("--seed", type=int, default=42)
    args = p.parse_args()
    main(args)