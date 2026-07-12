"""
handlers/__init__.py

Register all Telegram handlers.

This module is the single entry point for registering
every handler used by the application.

Whenever a new handler is added, it should be imported
and registered here. No other module should register
handlers directly.
"""

# Import Telegram classes.
#
# Application is the main Telegram application object.
# CommandHandler connects Telegram commands to handler
# functions.
from telegram.ext import (
    Application,
    CommandHandler,
)

# Import Telegram commands.
#
# Command names are stored separately to avoid
# hardcoding strings throughout the project.
from app.commands import (
    START,
    HELP,
    PRICE,
)

# Import handler functions.
#
# Every command has its own dedicated handler module.
from app.handlers.start import start_handler

# These handlers will be created later.
#
# Uncomment the imports after the files exist.
#
# from app.handlers.help import help_handler
# from app.handlers.price import price_handler


def register_handlers(
    application: Application,
) -> None:
    """
    Register every Telegram handler.

    Args:
        application:
            The Telegram Application instance.

    Returns:
        None.
    """

    # ======================================================
    # /start
    # ======================================================

    application.add_handler(
        CommandHandler(
            START,
            start_handler,
        )
    )

    # ======================================================
    # /help
    # ======================================================

    # Uncomment after help.py is implemented.
    #
    # application.add_handler(
    #     CommandHandler(
    #         HELP,
    #         help_handler,
    #     )
    # )

    # ======================================================
    # /price
    # ======================================================

    # Uncomment after price.py is implemented.
    #
    # application.add_handler(
    #     CommandHandler(
    #         PRICE,
    #         price_handler,
    #     )
    # )