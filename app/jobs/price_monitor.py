"""
price_monitor.py

Monitor Torob prices and notify only when price changes.
"""

import logging
from pathlib import Path

from telegram.ext import ContextTypes

from app.scrapers.torob import get_price

logger = logging.getLogger(__name__)

PRODUCT_URL = (
    "https://torob.com/p/f498b27b-596c-47c8-a48d-0beed264b2d8/"
)

CHAT_ID = 625896200

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

PRICE_FILE = DATA_DIR / "last_price.txt"


def load_last_price() -> str | None:
    """
    Load previous price from file.
    """

    if not PRICE_FILE.exists():
        return None

    return PRICE_FILE.read_text(
        encoding="utf-8"
    ).strip()


def save_price(price: str) -> None:
    """
    Save latest price.
    """

    PRICE_FILE.write_text(
        price,
        encoding="utf-8",
    )


async def monitor_price(
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    """
    Check product price.
    Send message only if changed.
    """

    try:

        data = await get_price(
            PRODUCT_URL
        )

        title = data["title"]
        seller = data["seller"]
        new_price = data["price"]

        old_price = load_last_price()

        # First run
        if old_price is None:

            save_price(new_price)

            await context.bot.send_message(
                chat_id=CHAT_ID,
                text=(
                    "Price monitor started.\n\n"
                    f"Product: {title}\n"
                    f"Current Price: {new_price}"
                ),
            )

            logger.info(
                "Initial price saved."
            )

            return

        # No change
        if old_price == new_price:

            logger.info(
                "Price unchanged."
            )

            return

        # Price changed
        save_price(new_price)

        message = (
            "PRICE CHANGED\n\n"
            f"Product:\n{title}\n\n"
            f"Seller:\n{seller}\n\n"
            f"Old Price:\n{old_price}\n\n"
            f"New Price:\n{new_price}"
        )

        await context.bot.send_message(
            chat_id=CHAT_ID,
            text=message,
        )

        logger.info(
            "Price change notification sent."
        )

    except Exception as error:

        logger.exception(error)