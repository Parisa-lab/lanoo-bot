"""
price_service.py

Business logic for product price searches.
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


class PriceService:
    """
    Product price search service.

    This class contains the business logic for
    product searches.

    Scrapers should not be called directly from
    Telegram handlers. Handlers should call this
    service instead.
    """

    async def search(
        self,
        query: str,
    ) -> Product:
        """
        Search for a product.

        Currently returns mock data.

        Future versions will:
        - Search Torob
        - Search Digikala
        - Search Emalls
        - Compare prices
        - Return the best result

        Args:
            query:
                Product search query.

        Returns:
            Product object.
        """

        # Log search request.
        logger.info(
            "Searching product: %s",
            query,
        )

        # --------------------------------------------------
        # Temporary fake product.
        # --------------------------------------------------

        product = Product(
            title=query,
            store="Test Store",
            price=89_900_000,
            url="https://example.com",
            image_url="",
        )

        # Log successful result.
        logger.info(
            "Search completed: %s",
            product.title,
        )

        return product