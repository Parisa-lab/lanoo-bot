"""
price_service.py

Business logic for product searches.
"""

# ==========================================================
# Standard Library Imports
# ==========================================================

import logging

# ==========================================================
# Local Imports
# ==========================================================

from app.models import Product
from app.scrapers import TorobScraper

# ==========================================================
# Logger
# ==========================================================

logger = logging.getLogger(__name__)


class PriceService:
    """
    Product price search service.
    """

    def __init__(self) -> None:
        """
        Initialize service.
        """

        self.torob = TorobScraper()

    async def search(
        self,
        query: str,
    ) -> Product:
        """
        Search product.

        Args:
            query:
                Product search query.

        Returns:
            Product.
        """

        logger.info(
            "Price search started: %s",
            query,
        )

        product = await self.torob.search(
            query,
        )

        logger.info(
            "Price search completed."
        )

        return product