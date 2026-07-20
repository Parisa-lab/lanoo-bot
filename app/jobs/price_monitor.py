"""
Price monitoring job for Lanoo.

This module periodically checks all tracked products stored in PostgreSQL
and sends Telegram notifications whenever a price change is detected.

Architecture:

PostgreSQL
↓
Repository Layer
↓
Price Monitor
↓
Telegram Notifications

Author: Lanoo
"""

import logging

from telegram.ext import ContextTypes

from app.database.repository import get_all_products
from app.database.repository import update_price
from app.scrapers.torob import get_price

logger = logging.getLogger(__name__)


async def check_prices(
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    """
    Check all tracked products and notify users when prices change.

    This job should be registered with the JobQueue and executed
    periodically (for example every 15 minutes).
    """

    try:
        products = await get_all_products()

        logger.info(
            "Checking %s tracked products",
            len(products),
        )

        for product in products:
            try:
                data = await get_price(
                    product.url,
                )

                if not data:
                    logger.warning(
                        "Failed to fetch product data: %s",
                        product.url,
                    )
                    continue

                current_price = str(
                    data["price"]
                )

                old_price = str(
                    product.last_price
                )

                if current_price == old_price:
                    continue

                await context.bot.send_message(
                    chat_id=product.chat_id,
                    text=(
                        "📉 Price Change Detected\n\n"
                        f"Product: {product.title}\n"
                        f"Old Price: {old_price}\n"
                        f"New Price: {current_price}\n\n"
                        f"{product.url}"
                    ),
                )

                await update_price(
                    product_id=product.id,
                    new_price=current_price,
                )

                logger.info(
                    "Price updated for product %s",
                    product.id,
                )

            except Exception:
                logger.exception(
                    "Failed processing product %s",
                    product.id,
                )

    except Exception:
        logger.exception(
            "Price monitor job failed",
        )