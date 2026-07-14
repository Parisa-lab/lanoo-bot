"""
torob.py

Torob scraper.

Currently returns mock data.

Later this scraper will fetch real product data
from Torob search results.
"""

# ==========================================================
# Standard Library Imports
# ==========================================================

import logging

# ==========================================================
# Local Imports
# ==========================================================

from app.models import Product

# ==========================================================
# Logger
# ==========================================================

logger = logging.getLogger(__name__)


class TorobScraper:
    """
    Torob scraper.
    """

    async def search(
        self,
        query: str,
    ) -> Product:
        """
        Search Torob.

        Args:
            query:
                Product name.

        Returns:
            Product.
        """

        logger.info(
            "Torob search started: %s",
            query,
        )

        # --------------------------------------------------
        # Temporary fake result.
        # --------------------------------------------------

        product = Product(
            title=query,
            store="Torob Test Store",
            price=87_500_000,
            url="https://torob.com",
            image_url="",
        )

        logger.info(
            "Torob search completed."
        )

        return product