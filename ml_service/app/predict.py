from app.models import load_model
from app.utils import featurize

def classify_transactions(df):
    clf = load_model("rf_classifier.joblib")
    X = featurize(df)
    probs = clf.predict_proba(X)
    labels = clf.classes_[probs.argmax(axis=1)]
    maxp = probs.max(axis=1)
    return labels, maxp

def anomaly_scores(df):
    iso = load_model("iso_forest.joblib")
    X = featurize(df)

    # predict: -1 = anomaly, 1 = normal
    preds = iso.predict(X)

    # Return boolean flags for simplicity
    results = [p == -1 for p in preds]
    return results
