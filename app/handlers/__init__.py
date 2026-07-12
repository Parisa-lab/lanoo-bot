"""
handlers package

This package contains all Telegram command handlers.

Each handler is responsible for exactly one command.
"""

# Import the /start command handler.
#
# This allows us to import it directly from
# the handlers package.
from .start import start


# Define the public objects of this package.
#
# __all__ tells Python which names should be
# exported when someone imports this package.
#
# This also makes the package interface clearer.
__all__ = [
    "start",
]