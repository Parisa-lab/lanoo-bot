"""
config.py

Load and validate application settings.

This module is the single source of truth for every
configuration value used by the application.

Configuration values are loaded from environment
variables or from a local .env file.

Never hardcode secrets such as API keys or tokens
inside the source code.
"""

# Import Python's logging module.
import logging

# Import field validator.
#
# Validators allow us to validate or transform
# configuration values before they are used.
from pydantic import field_validator

# Import Pydantic Settings.
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


class Settings(BaseSettings):
    """
    Application settings.

    Every configurable value should be defined here.

    Values are loaded in the following order:

    1. Environment variables
    2. .env file
    3. Default values
    """

    # Configure Pydantic Settings.
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False,
    )

    # ======================================================
    # Telegram
    # ======================================================

    # Telegram Bot Token.
    #
    # This value is required.
    bot_token: str

    # ======================================================
    # Application
    # ======================================================

    # Current application environment.
    #
    # Allowed values typically include:
    #
    # development
    # testing
    # production
    environment: str = "production"

    # Enable or disable debug mode.
    debug: bool = False

    # ======================================================
    # Logging
    # ======================================================

    # Default logging level.
    #
    # Environment examples:
    #
    # LOG_LEVEL=INFO
    # LOG_LEVEL=DEBUG
    # LOG_LEVEL=WARNING
    log_level: int = logging.INFO

    # ======================================================
    # Network
    # ======================================================

    # HTTP request timeout in seconds.
    request_timeout: int = 30

    # Maximum simultaneous HTTP connections.
    max_connections: int = 20

    # ======================================================
    # Scraper
    # ======================================================

    # Delay between scraper requests.
    scraper_delay: float = 1.0

    # ======================================================
    # Cache
    # ======================================================

    # Cache lifetime in seconds.
    cache_ttl: int = 300

    # ======================================================
    # Validators
    # ======================================================

    @field_validator("log_level", mode="before")
    @classmethod
    def validate_log_level(cls, value: object) -> int:
        """
        Convert log level names into logging constants.

        Examples:

        INFO      -> logging.INFO
        DEBUG     -> logging.DEBUG
        WARNING   -> logging.WARNING
        ERROR     -> logging.ERROR
        CRITICAL  -> logging.CRITICAL
        """

        # Already an integer.
        if isinstance(value, int):
            return value

        # Convert strings.
        if isinstance(value, str):

            level = value.upper()

            mapping = {
                "DEBUG": logging.DEBUG,
                "INFO": logging.INFO,
                "WARNING": logging.WARNING,
                "ERROR": logging.ERROR,
                "CRITICAL": logging.CRITICAL,
            }

            if level in mapping:
                return mapping[level]

        raise ValueError(
            "Invalid LOG_LEVEL value."
        )


# Create a shared Settings instance.
#
# Every module should import this object.
settings = Settings()