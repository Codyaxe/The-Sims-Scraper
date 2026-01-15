@echo off
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python 3.6 or higher.
    pause
    exit /b
)
python -m venv venv
call venv\Scripts\activate
pip install requests beautifulsoup4