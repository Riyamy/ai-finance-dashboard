# start-all.ps1 - run from project root
# Opens three PowerShell windows and starts ML service, backend, and frontend

# Resolve project root from script location
$root = Split-Path -Parent $MyInvocation.MyCommand.Definition

# 1) ML service (activate venv then run uvicorn)
Start-Process powershell -ArgumentList '-NoExit','-Command', "cd `"$root\ml_service`"; . `"$root\ml_service\.venv\Scripts\Activate.ps1`"; uvicorn app.main:app --reload --port 8000"

# 2) Backend (Node)
Start-Process powershell -ArgumentList '-NoExit','-Command', "cd `"$root\backend`"; npm run dev"

# 3) Frontend (React)
Start-Process powershell -ArgumentList '-NoExit','-Command', "cd `"$root\frontend`"; npm start"
