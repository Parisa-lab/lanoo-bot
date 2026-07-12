"""
main.py

Project entry point.

This file is intentionally kept very small.

Its only responsibility is to start the application.

All business logic lives inside the app package.
"""

# Import the function that starts the Telegram bot.
#
# We DO NOT write the startup code here.
#
# Instead, we import it from app.bot.
#
# Why?
#
# Because every file should have only ONE responsibility.
#
# main.py should only start the project.
#
# app.bot should know HOW to start the bot.
#
from app.bot import run_bot


# __name__ is a special variable created automatically by Python.
#
# Every Python file has this variable.
#
# If Python runs THIS file directly,
#
#     python main.py
#
# then __name__ becomes "__main__"
#
# But if another file imports main.py,
#
# __name__ becomes "main"
#
# This prevents the bot from starting automatically
# when another file imports main.py.
#
if __name__ == "__main__":

    # Start the Telegram bot.
    #
    # This calls the function located inside app.bot.
    #
    run_bot()