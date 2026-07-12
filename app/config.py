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

   