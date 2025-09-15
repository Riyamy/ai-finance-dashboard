# 💰 AI-Powered Personal Finance Dashboard

A **full-stack application** that provides deep insights into personal spending habits using **Machine Learning**.  
It automatically categorizes transactions, detects anomalies (fraud/unusual activity), and gives predictive financial insights.

---

## ✨ Features

### 🤖 Machine Learning
- **Transaction Categorization** — Random Forest Classifier, ~95% accuracy.  
- **Anomaly Detection** — Isolation Forest for fraud detection.  
- **Savings Insights** — Predictive pipeline for spending optimization.

### 📊 Dashboard
- Interactive **line & pie charts** (React + Recharts).  
- Simulate new transactions and view live predictions.  
- Category breakdown + anomaly flags per transaction.  

### 🛠 Tech Stack
- **Frontend** — React, Recharts, Context API  
- **Backend** — Node.js + Express  
- **ML Service** — Python (FastAPI, Scikit-learn, Pandas, NumPy)  
- **Database** — In-memory (demo) → ready for MongoDB/Postgres  

---

## 🚀 Quick Start (Windows PowerShell)
Prerequisites
- [Python 3.11+](https://www.python.org/downloads/)  
- [Node.js 18+](https://nodejs.org/)  
- [Git](https://git-scm.com/)  

---

1. Allow PowerShell scripts (first time only)
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

2. Start all services with one script

   From project root:

   .\start-all.ps1


This opens 3 PowerShell windows:

ML Service → http://127.0.0.1:8000

Backend → http://127.0.0.1:4000/api

Frontend → http://localhost:3000

3. Manual run (alternative)
   ML Service (Python + FastAPI)
   cd ml_service
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   pip install -r requirements.txt

# generate synthetic training data
python .\data\generate_data.py --out .\data\demo.csv --n 5000

# train models (saved in ../models)
python -m app.train --data .\data\demo.csv --out_dir ..\models

# run ML service
uvicorn app.main:app --reload --port 8000


Health check:

Invoke-WebRequest -Uri "http://127.0.0.1:8000/health" | Select-Object -ExpandProperty Content

Backend (Node.js + Express)
cd backend
npm install
npm run dev


Health check:

Invoke-WebRequest -Uri "http://127.0.0.1:4000/api/transactions" | Select-Object -ExpandProperty Content

Frontend (React)
cd frontend
npm install
# create .env file if missing:
# REACT_APP_API_BASE=http://127.0.0.1:4000/api
npm start


Open: http://localhost:3000

4. Quick Tests

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

(Optional) Docker Compose
docker-compose up --build

Verification Checklist

✅ ML service responds at http://127.0.0.1:8000/health

✅ Backend responds at http://127.0.0.1:4000/api/transactions

✅ Frontend dashboard loads at http://localhost:3000

✅ Charts update when simulating new transactions

Repository Structure
personal-finance-dashboard/
│── backend/        # Node.js Express API
│── frontend/       # React Dashboard
│── ml_service/     # FastAPI ML service
│── models/         # Saved ML models (after training)
│── docker-compose.yml
│── start-all.ps1   # Windows helper script
│── README.md
│── .gitignore















```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
