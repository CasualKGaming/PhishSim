python --version | Out-Null

if (-Not (Test-Path ".\.venv")) {
  python -m venv .venv
}

. .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r backend\requirements.txt

Write-Host "✅ Setup complete. Use '.\scripts\run.ps1' to start the API." -ForegroundColor Green
