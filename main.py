"""
main.py

Application entry point.

This module is responsible for starting the Telegram bot.

Execution starts here when the application is launched.
"""

# Import Python's logging module.
#
# Used to report unexpected startup errors.
import logging
import sys

# Import the Telegram bot.
from app.bot import LanooBot


# Create a logger for this module.
logger = logging.getLogger(__name__)


def main() -> None:
    """
    Start the application.

    This function creates the Telegram bot and starts
    the polling loop.

    Returns:
        None.
    """

    try:
        # Create the bot instance.
        bot = LanooBot()

        # Start the bot.
        bot.run()

    except KeyboardInterrupt:
        # The application was stopped manually.
        logger.info("Application stopped by user.")

    except Exception:
        # Log the complete exception traceback.
        logger.exception(
            "Application terminated because of an unexpected error."
        )

        # Exit with a non-zero status code.
        sys.exit(1)


if __name__ == "__main__":
    main()