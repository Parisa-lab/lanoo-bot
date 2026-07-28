"""
Price monitoring service.

Responsible for:

- loading tracked products
- checking current prices
- detecting changes
- notifying users
- updating database
"""

from __future__ import annotations

import logging

from app.repositories.product_repository import (
    ProductRepository,
)
from app.scrapers import TorobScraper
from app.services.notification_service import (
    NotificationService,
)

logger = logging.getLogger(__name__)


class MonitoringService:

    def __init__(
        self,
        repository: ProductRepository,
        scraper: TorobScraper,
        notifications: NotificationService,
    ) -> None:

        self.repository = repository
        self.scraper = scraper
        self.notifications = notifications

    @staticmethod
    def normalize_price(
        price: str,
    ) -> int:

        persian_digits = "۰۱۲۳۴۵۶۷۸۹"
        english_digits = "0123456789"

        translation = str.maketrans(
            persian_digits,
            english_digits,
        )

        cleaned = (
            str(price)
            .translate(translation)
            .replace("٬", "")
            .replace(",", "")
            .replace("٫", "")
            .replace(".", "")
            .replace("تومان", "")
            .replace(" ", "")
        )

        digits = "".join(
            c
            for c in cleaned
            if c.isdigit()
        )

        return int(digits) if digits else 0

    async def check_prices(self) -> None:

        products = (
            await self.repository.get_all_products()
        )

        logger.info(
            "Checking %s products",
            len(products),
        )

        for product in products:

            data = await self.scraper.get_price(
                product.url,
            )

            if not data:
                continue

            current_price = str(
                data["price"]
            )

            old_price = str(
                product.last_price
            )

            current_num = self.normalize_price(
                current_price
            )

            old_num = self.normalize_price(
                old_price
            )

            if (
                current_num == 0
                or old_num == 0
            ):
                continue

            if current_num == old_num:
                continue

            await self.notifications.send_price_change(
                chat_id=product.chat_id,
                product_title=product.title,
                old_price=old_price,
                new_price=current_price,
                url=product.url,
            )

            await self.repository.update_price(
                product.id,
                current_price,
            )

            logger.info(
                "Price updated for product %s",
                product.id,
            )