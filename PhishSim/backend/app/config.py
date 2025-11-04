from pydantic import BaseModel
import os

class Settings(BaseModel):
    secret_key: str = os.getenv("SECRET_KEY", "devsecret")
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 60 * 24

    db_engine: str = os.getenv("DB_ENGINE", "sqlite").lower()
    sqlite_path: str = os.getenv("SQLITE_PATH", "./phishsim.db")

    postgres_user: str = os.getenv("POSTGRES_USER", "phish")
    postgres_password: str = os.getenv("POSTGRES_PASSWORD", "phishpass")
    postgres_db: str = os.getenv("POSTGRES_DB", "phishdb")
    postgres_host: str = os.getenv("POSTGRES_HOST", "localhost")
    postgres_port: int = int(os.getenv("POSTGRES_PORT", "5432"))

settings = Settings()
