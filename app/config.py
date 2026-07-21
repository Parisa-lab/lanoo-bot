"""
Application configuration.

Loads environment variables from .env
and provides strongly typed settings.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Global application settings.
    """

    bot_token: str

    database_url: str = (
        "sqlite+aiosqlite:///./lanoo.db"
    )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()