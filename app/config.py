"""
config.py

Application configuration.

This module is responsible for loading all configuration
values required by the application.

Configuration values are read from environment variables
instead of being hardcoded in the source code.
"""

# Import Python's built-in operating system module.
#
# The os module allows Python to interact with the operating system.
#
# One of its features is reading environment variables.
import os


# Read the Telegram bot token from the environment.
#
# Railway stores secret values as environment variables.
#
# Example:
#
# BOT_TOKEN = 123456789:AA......
#
# We NEVER put this token directly inside our code.
#
# os.getenv("BOT_TOKEN") means:
#
# "Find an environment variable called BOT_TOKEN.
# If it exists, return its value.
# Otherwise, return None."
BOT_TOKEN = os.getenv("BOT_TOKEN")


# Check whether the token was found.
#
# If BOT_TOKEN is None,
# the application cannot connect to Telegram.
#
# Instead of failing later,
# we stop immediately and show a clear error message.
if BOT_TOKEN is None:

    # Raise an exception.
    #
    # RuntimeError tells Python that the program
    # cannot continue because something important
    # is missing.
    raise RuntimeError(
        "BOT_TOKEN environment variable is missing."
    ) 