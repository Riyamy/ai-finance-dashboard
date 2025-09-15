# 💰 AI-Powered Personal Finance Dashboard

A full-stack project that uses **Machine Learning + React + Node.js** to analyze personal spending habits.  
It categorizes transactions, detects anomalies (fraud/unusual activity), and shows insights in an interactive dashboard.

---

## ✨ Features
- **ML Models**: Random Forest (transaction categorization, ~95% accuracy) + Isolation Forest (fraud detection)  
- **Dashboard**: Interactive line & pie charts for spending trends (React + Recharts)  
- **Backend**: Node.js + Express REST API  
- **ML Service**: Python FastAPI + Scikit-learn  
- **Database**: In-memory (demo), ready for MongoDB/Postgres  

---

## 🚀 Quick Start (Windows)

### 1. Prerequisites
- Python 3.11+  
- Node.js 18+  
- Git  

### 2. Allow PowerShell scripts (first time only)
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
### 3. Start all services (easiest)

From project root:
.\start-all.ps1
This opens 3 windows:

ML Service → http://127.0.0.1:8000

Backend → http://127.0.0.1:4000/api

Frontend → http://localhost:3000
🛠 Manual Run (if needed)
ML Service
cd ml_service
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python .\data\generate_data.py --out .\data\demo.csv --n 5000
python -m app.train --data .\data\demo.csv --out_dir ..\models
uvicorn app.main:app --reload --port 8000

Backend
cd backend
npm install
npm run dev

Frontend
cd frontend
npm install
# .env should contain:
# REACT_APP_API_BASE=http://127.0.0.1:4000/api
npm start

✅ Quick Test

Ingest a transaction:

Invoke-WebRequest -Uri "http://127.0.0.1:4000/api/transactions/ingest" `
-Method POST -ContentType "application/json" `
-Body '{"amount":150,"merchant":"Amazon","description":"books"}' |
Select-Object -ExpandProperty Content


Example response:

{
  "amount": 150,
  "merchant": "Amazon",
  "description": "books",
  "category": "normal",
  "prob": 0.42,
  "is_anomaly": false
}

📂 Repository Structure
personal-finance-dashboard/
│── backend/        # Node.js Express API
│── frontend/       # React Dashboard
│── ml_service/     # FastAPI ML service
│── models/         # Saved ML models
│── docker-compose.yml
│── start-all.ps1
│── README.md
│── .gitignore


