from __future__ import annotations

from functools import lru_cache

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env", "apps/api/.env"),
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_name: str = "TinyFish AI Mock Interview"
    app_env: str = "local"
    app_host: str = "0.0.0.0"
    app_port: int = 8000
    debug: bool = True
    backend_cors_origins: list[str] = Field(
        default=["http://localhost:3000", "http://127.0.0.1:3000"],
        alias="BACKEND_CORS_ORIGINS",
    )

    database_url: str = Field(default="sqlite:///./tinyfish_ai.db", alias="DATABASE_URL")
    sqlite_fallback_url: str = Field(default="sqlite:///./tinyfish_ai.db", alias="SQLITE_FALLBACK_URL")

    supabase_url: str | None = Field(default=None, alias="SUPABASE_URL")
    supabase_anon_key: str | None = Field(default=None, alias="SUPABASE_ANON_KEY")
    supabase_service_role_key: str | None = Field(default=None, alias="SUPABASE_SERVICE_ROLE_KEY")

    openai_api_key: str | None = Field(default=None, alias="OPENAI_API_KEY")
    openai_model: str = Field(default="gpt-4o-mini", alias="OPENAI_MODEL")
    openai_base_url: str = Field(default="https://api.openai.com/v1", alias="OPENAI_BASE_URL")

    tinyfish_api_key: str | None = Field(default=None, alias="TINYFISH_API_KEY")
    tinyfish_base_url: str = Field(default="https://api.tinyfish.ai", alias="TINYFISH_BASE_URL")
    tinyfish_timeout_seconds: int = Field(default=45, alias="TINYFISH_TIMEOUT_SECONDS")
    tinyfish_stealth: bool = Field(default=True, alias="TINYFISH_STEALTH")
    tinyfish_use_mock: bool = Field(default=True, alias="TINYFISH_USE_MOCK")

    @field_validator("backend_cors_origins", mode="before")
    @classmethod
    def parse_cors_origins(cls, value):
        if isinstance(value, str):
            return [item.strip() for item in value.split(",") if item.strip()]
        return value


@lru_cache
def get_settings() -> Settings:
    return Settings()
