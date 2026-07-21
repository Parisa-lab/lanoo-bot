"""
Application configuration.

Loads environment variables from .env
and provides strongly typed application settings.

The application uses PostgreSQL in production.
Database credentials are never hardcoded here.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Global application settings.

    Values are loaded from environment variables
    or the local .env file during development.
    """

    # Telegram bot authentication token.
    bot_token: str

    # PostgreSQL database connection URL.
    #
    # Expected format:
    # postgresql+asyncpg://user:password@host:port/database
    #
    # Railway automatically provides DATABASE_URL.
    database_url: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


# Singleton settings instance used across the application.
settings = Settings()