"""
price_service.py

Business logic for product price searches.
"""

# ==========================================================
# Standard Library Imports
# ==========================================================

import logging

# ==========================================================
# Logger
# ==========================================================

logger = logging.getLogger(__name__)


class PriceService:
    """
    Product price search service.
    """

    async def search(
        self,
        query: str,
    ) -> str:
        """
        Search product prices.

        Args:
            query:
                Product search query.

        Returns:
            Formatted result text.
        """

        logger.info(
            "Searching prices for: %s",
            query,
        )

        # Temporary fake data.
        return (
            "🔍 Search Result\n\n"
            f"Product: {query}\n"
            "Store: Test Store\n"
            "Price: 89,900,000 Toman"
        )