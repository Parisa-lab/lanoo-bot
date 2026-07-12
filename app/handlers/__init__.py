"""
handlers package

Register all Telegram command handlers.

This module acts as the single entry point for every
Telegram handler used by the application.

When a new handler is added, it only needs to be
imported and registered here.

The rest of the application never needs to change.
"""

# Import Telegram classes.
#
# Application is the central object used to register
# command handlers.
from telegram.ext import (
    Application,
    CommandHandler,
)

# Import command names.
#
# Keeping command names inside constants.py avoids
# hardcoding strings throughout the project.
from app.constants import (
    START_COMMAND,
    HELP_COMMAND,
    PRICE_COMMAND,
)

# Import handler functions.
from .start import start_handler

# The following handlers will be implemented later.
#
# Uncomment these imports when the files are created.
#
# from .help import help_handler
# from .price import price_handler


def register_handlers(
    application: Application,
) -> None:
    """
    Register every Telegram command handler.

    Args:
        application:
            The Telegram Application instance.

    Returns:
        None
    """

    # ==============================================
    # /start
    # ==============================================

    application.add_handler(
        CommandHandler(
            START_COMMAND,
            start_handler,
        )
    )

    # ==============================================
    # /help
    # ==============================================

    # application.add_handler(
    #     CommandHandler(
    #         HELP_COMMAND,
    #         help_handler,
    #     )
    # )

    # ==============================================
    # /price
    # ==============================================

    # application.add_handler(
    #     CommandHandler(
    #         PRICE_COMMAND,
    #         price_handler,
    #     )
    # )