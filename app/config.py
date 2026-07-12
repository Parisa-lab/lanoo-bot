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

# Import the logging module.
#
# Logging constants such as logging.INFO are used
# as default values for the application.
import logging

# Import BaseSettings.
#
# BaseSettings automatically loads configuration
# values from environment variables.
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
    #
    # Railway ignores the .env file and injects
    # environment variables automatically.
    #
    # During local development, values are loaded
    # from the .env file if it exists.
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # ======================================================
    # Telegram
    # ======================================================

    # Telegram Bot Token.
    #
    # This value is required.
    # The application cannot start without it.
    bot_token: str

    # ======================================================
    # Application
    # ======================================================

    # Current application environment.
    #
    # Typical values:
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
    # Available values:
    #
    # logging.DEBUG
    # logging.INFO
    # logging.WARNING
    # logging.ERROR
    # logging.CRITICAL
    log_level: int = logging.INFO

    # ======================================================
    # Network
    # ======================================================

    # Maximum time to wait for HTTP requests.
    request_timeout: int = 30

    # Maximum simultaneous HTTP connections.
    max_connections: int = 20

    # ======================================================
    # Scraper
    # ======================================================

    # Delay between HTTP requests.
    #
    # This helps avoid sending requests too quickly.
    scraper_delay: float = 1.0

    # ======================================================
    # Cache
    # ======================================================

    # Cache lifetime in seconds.
    cache_ttl: int = 300


# Create a shared Settings instance.
#
# Import this object everywhere instead of creating
# additional Settings instances.
settings = Settings()