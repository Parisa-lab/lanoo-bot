"""
app/services/price_service.py

Application service for product operations.

Responsibilities:
- Product lookup
- Product tracking
- Business rules

Database access is delegated to repositories.
"""

from __future__ import annotations

import logging
from typing import Any

from app.repositories.product_repository import ProductRepository
from app.scrapers import TorobScraper

logger = logging.getLogger(__name__)


class PriceService:
    """
    Product application service.
    """

    def __init__(
        self,
        scraper: TorobScraper | None = None,
        repository: ProductRepository | None = None,
    ) -> None:

        self.scraper = scraper or TorobScraper()

        self.repository = (
            repository
            or ProductRepository()
        )

    async def search(
        self,
        url: str,
    ) -> dict[str, Any] | None:

        if not url:
            return None

        return await self.scraper.get_price(url)

    async def is_tracked(
        self,
        chat_id: int,
        url: str,
    ) -> bool:

        product = await self.repository.get_product_by_url(
            chat_id=chat_id,
            url=url,
        )

        return product is not None

    async def track_product(
        self,
        chat_id: int,
        url: str,
    ) -> dict[str, Any] | None:

        data = await self.search(url)

        if not data:
            return None

        exists = await self.is_tracked(
            chat_id=chat_id,
            url=url,
        )

        if not exists:

            await self.repository.add_product(
                chat_id=chat_id,
                url=url,
                title=data["title"],
                price=data["price"],
            )

        return data