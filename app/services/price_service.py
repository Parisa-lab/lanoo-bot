"""
app/services/price_service.py

Business logic for product lookups and tracking.

Responsibilities:
- Validate URLs
- Call Torob scraper
- Save products
- Check if products already exist
- Return product information

Handlers should never call repository functions directly.
"""

from __future__ import annotations

import logging
from typing import Any

from app.database.repository import add_product
from app.database.repository import get_product_by_url
from app.scrapers import TorobScraper

logger = logging.getLogger(__name__)


class PriceService:
    """
    Main application service for products.
    """

    def __init__(
        self,
        scraper: TorobScraper | None = None,
    ) -> None:

        self.torob = scraper or TorobScraper()

    async def search(
        self,
        url: str,
    ) -> dict[str, Any] | None:
        """
        Scrape product information.

        Returns:
            Product data dictionary or None.
        """

        if not isinstance(url, str):
            return None

        url = url.strip()

        if not url:
            return None

        logger.info(
            "Searching product: %s",
            url,
        )

        return await self.torob.get_price(url)

    async def is_tracked(
        self,
        chat_id: int,
        url: str,
    ) -> bool:
        """
        Check whether a product is already tracked.
        """

        product = await get_product_by_url(
            chat_id=chat_id,
            url=url,
        )

        return product is not None

    async def track_product(
        self,
        chat_id: int,
        url: str,
    ) -> dict[str, Any] | None:
        """
        Scrape and save a product.

        Returns:
            Product data if successful.
        """

        data = await self.search(url)

        if not data:
            return None

        already_exists = await self.is_tracked(
            chat_id=chat_id,
            url=url,
        )

        if already_exists:
            return data

        await add_product(
            chat_id=chat_id,
            url=url,
            title=data["title"],
            price=data["price"],
        )

        logger.info(
            "Tracked new product. chat_id=%s url=%s",
            chat_id,
            url,
        )

        return data