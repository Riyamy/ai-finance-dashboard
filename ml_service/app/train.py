import pandas as pd
from sklearn.ensemble import RandomForestClassifier, IsolationForest
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score
from app.utils import featurize
from app.models import save_model
import numpy as np
import argparse

def main(data_path, out_dir):
    # Load dataset
    df = pd.read_csv(data_path).fillna("")

    # Target + features
    y = df["label"].values
    X = featurize(df)

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # --- Train classifier ---
    clf = RandomForestClassifier(n_estimators=200, random_state=42)
    clf.fit(X_train, y_train)
    preds = clf.predict(X_test)
    acc = accuracy_score(y_test, preds)

    # --- Train anomaly detector ---
    normal_mask = y_train == "normal"
    iso = IsolationForest(n_estimators=100, contamination=0.01, random_state=42)
    iso.fit(X_train[normal_mask])

    # --- Save models ---
    clf_path = save_model(clf, "rf_classifier.joblib")
    iso_path = save_model(iso, "iso_forest.joblib")

    # --- Evaluate anomaly detection ---
    y_test_anom = np.array([0 if v == "normal" else 1 for v in y_test])
    preds_anom = (iso.predict(X_test) == -1).astype(int)  # -1 anomaly → 1
    precision = precision_score(y_test_anom, preds_anom, zero_division=0)

    # --- Print results ---
    print(f"RandomForest accuracy: {acc:.4f}")
    print(f"IsolationForest precision: {precision:.4f}")
    print(f"Saved classifier to: {clf_path}")
    print(f"Saved isolation forest to: {iso_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", required=True)
    parser.add_argument("--out_dir", default="../models")
    args = parser.parse_args()
    main(args.data, args.out_dir)
