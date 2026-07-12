"""
config.py

Load and validate application configuration.

This module is the single source of truth for all
configuration values used by the application.

Configuration is loaded from environment variables
or from a local .env file.

Never hardcode secrets such as API keys or tokens
inside the source code.
"""

# Import Python's logging module.
#
# Logging constants are used as default values.
import logging

# Import Pydantic validator.
#
# Validators allow configuration values to be
# validated or transformed before use.
from pydantic import field_validator

# Import Pydantic Settings.
#
# BaseSettings automatically loads values from
# environment variables and from a local .env file.
from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)


class Settings(BaseSettings):
    """
    Application settings.

    Every configurable value used by the application
    should be defined in this class.
    """

    # Configure how settings are loaded.
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False,
    )

    # ==================================================
    # Telegram
    # ==================================================

    # Telegram Bot Token.
    #
    # This value is required.
    bot_token: str

    # ==================================================
    # Application
    # ==================================================

    # Current application environment.
    #
    # Examples:
    # development
    # testing
    # production
    environment: str = "production"

    # Enable debug mode.
    debug: bool = False

    # ==================================================
    # Logging
    # ==================================================

    # Default logging level.
    #
    # Environment example:
    #
    # LOG_LEVEL=DEBUG
    #
    # Supported values:
    #
    # DEBUG
    # INFO
    # WARNING
    # ERROR
    # CRITICAL
    log_level: int = logging.INFO

    # ==================================================
    # Network
    # ==================================================

    # HTTP request timeout (seconds).
    request_timeout: int = 30

    # Maximum simultaneous HTTP connections.
    max_connections: int = 20

    # ==================================================
    # Scraper
    # ==================================================

    # Delay between scraper requests (seconds).
    scraper_delay: float = 1.0

    # ==================================================
    # Cache
    # ==================================================

    # Cache lifetime (seconds).
    cache_ttl: int = 300

    # ==================================================
    # Validators
    # ==================================================

    @field_validator("log_level", mode="before")
    @classmethod
    def validate_log_level(cls, value: object) -> int:
        """
        Convert logging level names into logging constants.
        """

        # Already a valid integer.
        if isinstance(value, int):
            return value

        # Convert string values.
        if isinstance(value, str):

            levels = {
                "DEBUG": logging.DEBUG,
                "INFO": logging.INFO,
                "WARNING": logging.WARNING,
                "ERROR": logging.ERROR,
                "CRITICAL": logging.CRITICAL,
            }

            level = levels.get(value.upper())

            if level is not None:
                return level

        raise ValueError(
            "Invalid LOG_LEVEL value."
        )


# Create one shared Settings instance.
#
# Import this object everywhere instead of creating
# additional Settings() instances.
settings = Settings()