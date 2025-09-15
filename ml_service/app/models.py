import joblib
from pathlib import Path

# Resolve the absolute models directory relative to project root
# e.g. personal-finance-dashboard/models
MODEL_DIR = Path(__file__).resolve().parents[2] / "models"
MODEL_DIR.mkdir(parents=True, exist_ok=True)

def save_model(obj, name: str):
    """
    Save a trained model to the models directory.
    Returns the saved path as string.
    """
    path = MODEL_DIR / name
    joblib.dump(obj, path)
    return str(path)

def load_model(name: str):
    """
    Load a model from the models directory.
    Raises FileNotFoundError if model does not exist.
    """
    path = MODEL_DIR / name
    if not path.exists():
        raise FileNotFoundError(f"Model '{name}' not found at {path}")
    return joblib.load(path)
