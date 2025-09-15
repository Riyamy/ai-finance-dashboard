import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import HashingVectorizer

# Fixed size used during training
EXPECTED_FEATURES = 68  

def featurize(df: pd.DataFrame):
    """
    Convert transaction DataFrame into numeric feature matrix for ML models.
    Automatically generates engineered features and ensures exactly
    EXPECTED_FEATURES (68) columns for both training & inference.
    """

    features = []

    # --- Numeric feature: amount ---
    amount = df.get("amount", 0).fillna(0).astype(float).values.reshape(-1, 1)
    features.append(amount)

    # --- Engineered feature: desc_length (length of description text) ---
    if "description" in df.columns:
        desc_length = df["description"].astype(str).fillna("").str.len().values.reshape(-1, 1)
    else:
        desc_length = np.zeros((len(df), 1))
    features.append(desc_length)

    # --- Engineered feature: high_amount (binary flag for unusually high transactions) ---
    if "amount" in df.columns:
        high_amount = (df["amount"].astype(float) > 500).astype(int).values.reshape(-1, 1)
    else:
        high_amount = np.zeros((len(df), 1))
    features.append(high_amount)

    # --- Engineered feature: merchant_id (hash bucket for merchants) ---
    if "merchant" in df.columns:
        merchant_id = df["merchant"].astype(str).fillna("").apply(lambda x: hash(x) % 1000).values.reshape(-1, 1)
    else:
        merchant_id = np.zeros((len(df), 1))
    features.append(merchant_id)

    # --- Text features (merchant + description) ---
    text = (
        df.get("merchant", "").astype(str).fillna("") + " " +
        df.get("description", "").astype(str).fillna("")
    )
    vec = HashingVectorizer(
        n_features=EXPECTED_FEATURES - 4,  # 1 numeric + 3 engineered
        alternate_sign=False
    )
    X_text = vec.transform(text.values).toarray()
    features.append(X_text)

    # --- Final feature matrix ---
    X = np.hstack(features)

    # --- Safety net: pad or truncate to EXACT size ---
    if X.shape[1] < EXPECTED_FEATURES:
        padding = np.zeros((X.shape[0], EXPECTED_FEATURES - X.shape[1]))
        X = np.hstack([X, padding])
    elif X.shape[1] > EXPECTED_FEATURES:
        X = X[:, :EXPECTED_FEATURES]

    return X
