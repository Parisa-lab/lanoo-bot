"""
bot.py

Create and start the Telegram bot.

This module is responsible for:

- Creating the Application object.
- Registering command handlers.
- Starting the bot.
"""

# Import the Application class.
#
# Application is the heart of every Telegram bot.
# It receives updates from Telegram and dispatches
# them to the correct command handlers.
from telegram.ext import Application


# Import the CommandHandler class.
#
# CommandHandler is responsible for commands such as:
#
# /start
# /help
# /price
#
# Each command will be connected to one function.
from telegram.ext import CommandHandler


# Import the bot token from config.py.
#
# The token is stored inside Railway
# as an environment variable.
#
# config.py reads it and makes it available here.
from app.config import BOT_TOKEN


# Import the function that handles the /start command.
#
# Whenever a user sends /start,
# this function will be executed.
from app.handlers import start


def run_bot() -> None:
    """
    Build and start the Telegram bot.
    """

    # Create the Telegram Application.
    #
    # Think of this as creating the bot itself.
    #
    # The builder() method creates a builder object.
    #
    # Then we provide the bot token.
    #
    # Finally, build() creates the Application instance.
    application = (
        Application
        .builder()
        .token(BOT_TOKEN)
        .build()
    )

    # Register the /start command.
    #
    # CommandHandler connects a Telegram command
    # to a Python function.
    #
    # When the user sends:
    #
    # /start
    #
    # Telegram will execute:
    #
    # start()
    #
    application.add_handler(
        CommandHandler(
            "start",
            start,
        )
    )

    # Print a message to the console.
    #
    # This helps us know that
    # the bot started successfully.
    print("Lanoo Bot started successfully.")

    # Start listening for Telegram updates.
    #
    # Polling means:
    #
    # "Telegram, do you have any new messages?"
    #
    # The bot asks Telegram this question
    # many times every second.
    #
    # If a new message arrives,
    # Telegram sends it back,
    # and the correct handler is executed.
    application.run_polling()