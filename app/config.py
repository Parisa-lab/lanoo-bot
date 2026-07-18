"""
config.py

Load and validate application configuration.
"""

import logging

from pydantic import field_validator
from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)


class Settings(BaseSettings):

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False,
    )

    # ==================================================
    # Telegram
    # ==================================================

    bot_token: str

    # ==================================================
    # Database
    # ==================================================

    database_url: str

    # ==================================================
    # Application
    # ==================================================

    environment: str = "production"

    debug: bool = False

    # ==================================================
    # Logging
    # ==================================================

    log_level: int = logging.INFO

    # ==================================================
    # Network
    # ==================================================

    request_timeout: int = 30

    max_connections: int = 20

    # ==================================================
    # Scraper
    # ==================================================

    scraper_delay: float = 1.0

    # ==================================================
    # Cache
    # ==================================================

    cache_ttl: int = 300

    # ==================================================
    # Validators
    # ==================================================

    @field_validator(
        "log_level",
        mode="before",
    )
    @classmethod
    def validate_log_level(
        cls,
        value: object,
    ) -> int:

        if isinstance(value, int):
            return value

        if isinstance(value, str):

            levels = {
                "DEBUG": logging.DEBUG,
                "INFO": logging.INFO,
                "WARNING": logging.WARNING,
                "ERROR": logging.ERROR,
                "CRITICAL": logging.CRITICAL,
            }

            level = levels.get(
                value.upper()
            )

            if level is not None:
                return level

        raise ValueError(
            "Invalid LOG_LEVEL value."
        )

    @field_validator(
        "database_url",
        mode="before",
    )
    @classmethod
    def normalize_database_url(
        cls,
        value: str,
    ) -> str:

        if value.startswith(
            "postgresql://"
        ):
            return value.replace(
                "postgresql://",
                "postgresql+asyncpg://",
                1,
            )

        return value


settings = Settings()