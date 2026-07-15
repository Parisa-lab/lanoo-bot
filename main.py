"""
main.py

Application entry point.
"""

from app.bot import LanooBot


def main() -> None:
    """
    Start Telegram bot.
    """

    bot = LanooBot()
    bot.run()


if __name__ == "__main__":
    main()