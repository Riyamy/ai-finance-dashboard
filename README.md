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
