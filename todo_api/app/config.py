from typing import Any, Dict, List, Optional

from pydantic import (AnyHttpUrl, BaseModel, BaseSettings, PostgresDsn,
                      validator)


class PostgresSettings(BaseModel):
    POSTGRES_DB: str = "postgres"
    POSTGRES_USER: str = "postgres"
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DATABASE: str = "postgres"
    POSTGRES_PORT: str = "5432"
    POSTGRES_CONNECTION_POOL_SIZE: int = 5
    POSTGRES_CONNECTION_MAX_OVERFLOW: int = 20

    URL: Optional[PostgresDsn] = None

    @validator("URL", pre=True)
    def get_url(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_HOST"),
            port=values.get("POSTGRES_PORT"),
            path=f"/{values.get('POSTGRES_DATABASE') or ''}",
        )


class Settings(BaseSettings):
    ENV: str = "local"
    LOG_LEVEL: str = "INFO"
    OPENAPI_URL: str = "/openapi.json"

    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = [
        "http://localhost",
        "http://localhost:3000",
    ]
    POSTGRES: PostgresSettings = PostgresSettings()

    class Config:
        case_sensitive = True


settings = Settings()
