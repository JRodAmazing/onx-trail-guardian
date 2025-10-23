@echo off
echo.
echo ============================================
echo   Trail Guardian Pro - Quick Setup
echo ============================================
echo.

REM Check if Docker is installed
docker --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Docker is not installed.
    echo Please install Docker Desktop from: https://www.docker.com/products/docker-desktop
    pause
    exit /b 1
)
echo [OK] Docker is installed

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed.
    echo Please install Python 3.11+ from: https://www.python.org/downloads/
    pause
    exit /b 1
)
echo [OK] Python is installed

echo.
echo Starting Docker services...
docker-compose up -d
if errorlevel 1 (
    echo [ERROR] Failed to start Docker services
    pause
    exit /b 1
)
echo [OK] Docker services started

echo.
echo Setting up Python environment...
cd backend

if not exist venv (
    python -m venv venv
    echo [OK] Virtual environment created
) else (
    echo [OK] Virtual environment already exists
)

call venv\Scripts\activate

echo.
echo Installing Python dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo [ERROR] Failed to install dependencies
    pause
    exit /b 1
)
echo [OK] Dependencies installed

echo.
echo Checking environment configuration...
if not exist .env (
    copy .env.example .env
    echo [WARNING] Created .env file - Please edit it and add your API keys!
    echo.
    echo You need:
    echo 1. NASA FIRMS API key: https://firms.modaps.eosdis.nasa.gov/api/
    echo 2. Mapbox token: https://account.mapbox.com/
    echo 3. Generate SECRET_KEY with: openssl rand -hex 32
    echo.
    pause
    notepad .env
)

echo.
echo ============================================
echo   Setup Complete!
echo ============================================
echo.
echo To start the API:
echo   1. Make sure .env has your API keys
echo   2. Run: uvicorn app.main:app --reload
echo.
echo Then visit: http://localhost:8000/docs
echo.
pause
