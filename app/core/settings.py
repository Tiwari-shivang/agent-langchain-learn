from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

PATH = Path(__file__).resolve().parents[2]

class Settings(BaseSettings):
    model_config=SettingsConfigDict(
        env_file=PATH / ".env",
        case_sensitive=False,
        extra="ignore"
    )
    DB_HOST: str
    DB_PORT: str
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str

def get_settings():
    return Settings()

settings = get_settings()