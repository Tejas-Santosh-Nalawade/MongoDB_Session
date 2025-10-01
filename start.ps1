# Student Management System - Quick Start Script
# Run this script to start both backend and frontend

Write-Host "🚀 Starting Student Management System..." -ForegroundColor Green

# Check if we're in the correct directory
if (-not (Test-Path "student-management-project")) {
    Write-Host "❌ Please run this script from the directory containing 'student-management-project' folder" -ForegroundColor Red
    exit 1
}

# Start backend in a new PowerShell window
Write-Host "📡 Starting Backend API Server..." -ForegroundColor Yellow
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd 'student-management-project/backend'; if (Test-Path 'venv') { venv\Scripts\activate } else { python -m venv venv; venv\Scripts\activate; pip install -r requirements.txt }; python app.py"

# Wait for backend to start
Write-Host "⏳ Waiting for backend to initialize..." -ForegroundColor Yellow
Start-Sleep -Seconds 5

# Start frontend in current window
Write-Host "🖥️  Starting Frontend Dashboard..." -ForegroundColor Yellow
Set-Location "student-management-project/frontend"

# Check if virtual environment exists, create if not
if (-not (Test-Path "venv")) {
    Write-Host "📦 Creating virtual environment and installing dependencies..." -ForegroundColor Cyan
    python -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt
} else {
    venv\Scripts\activate
}

Write-Host "🌟 Starting Streamlit Dashboard..." -ForegroundColor Green
Write-Host "📱 Frontend will open at: http://localhost:8501" -ForegroundColor Cyan
Write-Host "🔗 Backend API running at: http://127.0.0.1:5000" -ForegroundColor Cyan

streamlit run streamlit_app.py