# PhishSim – Windows Development Build

A full phishing simulation backend scaffold for **Windows**, built with **FastAPI + SQLite** for local development.

## Quick Start
1. Open PowerShell in this folder.
2. Run setup:
```powershell
.\scripts\setup.ps1
```
3. Start API:
```powershell
.\scriptsun.ps1
```
4. Open Swagger UI → http://localhost:8000/docs

## Default Features
- SQLite database (no external setup)
- JWT Authentication (register/login)
- CRUD for Campaigns & Templates
- Password hashing (bcrypt)
- Environment-configurable DB engine (SQLite or Postgres-ready)

## Folder Structure
```
backend/
  app/
    routers/ (API endpoints)
    models.py (SQLAlchemy models)
    schemas.py (Pydantic)
    auth.py (JWT helpers)
    database.py, main.py, config.py
scripts/
  setup.ps1 / setup.bat
  run.ps1 / run.bat
```

## Switching to Postgres (optional)
1. Install Postgres or Docker Desktop.
2. Edit `.env`:
```
DB_ENGINE=postgres
POSTGRES_USER=phish
POSTGRES_PASSWORD=phishpass
POSTGRES_DB=phishdb
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```
3. Restart API. SQLAlchemy auto-detects engine.
