import json, sys, joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report, roc_auc_score
from config import DATA, OUT, FIGURES, MODELS, MODEL, META, METRICS, TARGET
from src.core import load_data, prepare, make_model

def main():
    if not DATA.exists():
        sys.exit(f"Dataset not found: {DATA}\nAdd your labelled CSV as data/water_potability.csv.")
    df = load_data(DATA)
    X, y = prepare(df, TARGET)
    stratify = y if y.value_counts().min() >= 2 else None
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=.2, random_state=42, stratify=stratify)
    model = make_model()
    model.fit(Xtr, ytr)
    pred = model.predict(Xte)
    metrics = {
        "accuracy": float(accuracy_score(yte, pred)),
        "precision_weighted": float(precision_score(yte, pred, average="weighted", zero_division=0)),
        "recall_weighted": float(recall_score(yte, pred, average="weighted", zero_division=0)),
        "f1_weighted": float(f1_score(yte, pred, average="weighted", zero_division=0)),
        "rows": int(len(df)), "train_rows": int(len(Xtr)), "test_rows": int(len(Xte)),
        "features": list(X.columns), "classification_report": classification_report(yte, pred, output_dict=True, zero_division=0)
    }
    try:
        metrics["roc_auc"] = float(roc_auc_score(yte, model.predict_proba(Xte)[:, 1]))
    except Exception:
        metrics["roc_auc"] = None
    for folder in (OUT, FIGURES, MODELS):
        folder.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, MODEL)
    with open(METRICS, "w") as f: json.dump(metrics, f, indent=2)
    info = {c: {"min": float(X[c].min()), "max": float(X[c].max()), "median": float(X[c].median())} for c in X.columns}
    with open(META, "w") as f:
        json.dump({"features": list(X.columns), "feature_info": info, "classes": [str(c) for c in model.classes_]}, f, indent=2)
    # Save diagnostic figures.
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from sklearn.metrics import ConfusionMatrixDisplay
    fig, ax = plt.subplots(figsize=(5, 4))
    ConfusionMatrixDisplay.from_estimator(model, Xte, yte, ax=ax)
    fig.tight_layout(); fig.savefig(FIGURES / "confusion_matrix.png", dpi=160); plt.close(fig)
    imp = model.named_steps["classifier"].feature_importances_
    order = imp.argsort()
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.barh([X.columns[i] for i in order], imp[order], color="#13A8B5")
    ax.set_title("Random Forest Feature Importance"); fig.tight_layout()
    fig.savefig(FIGURES / "feature_importance.png", dpi=160); plt.close(fig)
    if "Potability" in df.columns:
        fig, ax = plt.subplots(figsize=(5, 4))
        df["Potability"].value_counts().sort_index().plot(kind="bar", ax=ax, color="#13A8B5")
        ax.set_title("Potability Class Distribution"); fig.tight_layout()
        fig.savefig(FIGURES / "target_distribution.png", dpi=160); plt.close(fig)
    numeric = df.select_dtypes("number")
    if numeric.shape[1] > 1:
        import seaborn as sns
        fig, ax = plt.subplots(figsize=(10, 7))
        sns.heatmap(numeric.corr(), cmap="vlag", center=0, ax=ax)
        ax.set_title("Correlation Heatmap"); fig.tight_layout()
        fig.savefig(FIGURES / "correlation_heatmap.png", dpi=160); plt.close(fig)
    print(f"Training complete. Test accuracy: {metrics['accuracy']:.3f}")
    print(f"Model: {MODEL}\nMetrics: {METRICS}\nFigures: {FIGURES}")

if __name__ == "__main__":
    main()
