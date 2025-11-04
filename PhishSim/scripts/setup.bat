@echo off
where python >nul 2>&1 || (echo Python not found.& exit /b 1)
if not exist .venv (
  python -m venv .venv
)
call .\.venv\Scripts\activate.bat
pip install --upgrade pip
pip install -r backend\requirements.txt
echo Setup complete. Run scripts\run.bat
