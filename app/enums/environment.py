"""
environment.py

Define the application environments.

Using an Enum instead of plain strings prevents
typing mistakes and improves code readability.
"""

# Import StrEnum.
#
# StrEnum behaves like both a string and an Enum.
# It is available in Python 3.11 and later.
from enum import StrEnum


class Environment(StrEnum):
    """
    Available application environments.
    """

    DEVELOPMENT = "development"

    TESTING = "testing"

    PRODUCTION = "production"