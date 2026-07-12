"""
config.py

Load application configuration.

This module centralizes all configuration values used by
the application.

Configuration is loaded from environment variables using
Pydantic Settings.

Advantages:

- Automatic validation
- Type safety
- Better error messages
- Easier maintenance
- Support for .env files
"""

# Import Pydantic Settings.
#
# BaseSettings automatically loads values from
# environment variables and .env files.
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


class Settings(BaseSettings):
    """
    Application settings.

    Every configuration value used by the application
    should be defined here.
    """

    # Configure Pydantic Settings.
    #
    # .env support is useful for local development.
    #
    # Railway ignores this file and uses its own
    # environment variables automatically.
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # ======================================================
    # Telegram Configuration
    # ======================================================

    # Telegram Bot Token.
    #
    # This value is required.
    # The application will fail to start if it is missing.
    bot_token: str


# Create one shared Settings instance.
#
# Every module should import this object instead of
# creating a new Settings() instance.
settings = Settings()