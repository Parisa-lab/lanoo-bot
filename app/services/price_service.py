"""
app/services/price_service.py

Business logic for Torob product lookups.

This service now uses the real TorobScraper class instead of importing a
non-existent class from the package.
"""

from __future__ import annotations

import logging
from typing import Any

from app.scrapers import TorobScraper

logger = logging.getLogger(__name__)


class PriceService:
    """
    Product price lookup service.

    This is intentionally thin:
    - validate input
    - call the scraper
    - return the scraped result
    """

    def __init__(self, scraper: TorobScraper | None = None) -> None:
        """
        Initialize the service.

        Args:
            scraper: Optional scraper instance for dependency injection.
        """
        self.torob = scraper or TorobScraper()

    async def search(self, url: str) -> dict[str, Any] | None:
        """
        Look up a Torob product page.

        Args:
            url: Torob product URL.

        Returns:
            Scraped product data or None.
        """
        if not isinstance(url, str) or not url.strip():
            logger.warning("PriceService.search received an invalid URL.")
            return None

        url = url.strip()

        logger.info("Price search started: %s", url)
        result = await self.torob.get_price(url)
        logger.info("Price search completed: %s", url)

        return result