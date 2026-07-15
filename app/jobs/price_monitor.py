"""
Automatic price monitoring.

Runs every hour.
"""

import logging

from telegram.ext import ContextTypes

from app.scrapers.torob import get_price

logger = logging.getLogger(__name__)

# Replace with your own values
CHAT_ID = 625896200

PRODUCTS = [
    "https://torob.com/p/f498b27b-596c-47c8-a48d-0beed264b2d8/",
]

LAST_PRICES = {}


async def check_prices(
    context: ContextTypes.DEFAULT_TYPE,
) -> None:

    for url in PRODUCTS:

        try:

            data = await get_price(url)

            title = data["title"]
            price = data["price"]

            old_price = LAST_PRICES.get(url)

            if old_price is None:

                LAST_PRICES[url] = price

                await context.bot.send_message(
                    chat_id=CHAT_ID,
                    text=(
                        "Product Added\n\n"
                        f"{title}\n\n"
                        f"Current Price: {price}"
                    ),
                )

                continue

            if old_price != price:

                await context.bot.send_message(
                    chat_id=CHAT_ID,
                    text=(
                        "Price Changed\n\n"
                        f"{title}\n\n"
                        f"Old Price: {old_price}\n"
                        f"New Price: {price}"
                    ),
                )

                LAST_PRICES[url] = price

        except Exception as error:

            logger.exception(error)