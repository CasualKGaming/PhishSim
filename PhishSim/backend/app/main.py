from fastapi import FastAPI
from .database import Base, engine
from .routers import auth_routes, templates_routes, campaigns_routes

app = FastAPI(title="PhishSim API", version="1.0")

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(auth_routes.router)
app.include_router(templates_routes.router)
app.include_router(campaigns_routes.router)
