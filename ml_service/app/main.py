from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
from typing import List
from app.predict import classify_transactions, anomaly_scores

app = FastAPI(title="ML Service")

class Transaction(BaseModel):
    amount: float
    merchant: str | None = None
    description: str | None = None
    timestamp: str | None = None
    category: str | None = None

@app.get('/health')
def health():
    return {"status": "ok"}

@app.post('/predict/transaction')
def predict_transaction(tx: Transaction):
    df = pd.DataFrame([tx.dict()])
    try:
        labels, probs = classify_transactions(df)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {"label": labels[0], "prob": float(probs[0])}

@app.post('/anomaly/check')
def check_anomaly(txs: List[Transaction]):
    df = pd.DataFrame([t.dict() for t in txs])
    try:
        flags = anomaly_scores(df)   # now returns [True/False]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {"results": [{"is_anomaly": bool(f)} for f in flags]}
