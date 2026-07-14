"""
message_formatter.py

Convert application models into Telegram messages.
"""

# ==========================================================
# Local Imports
# ==========================================================

from app.models import Product


class MessageFormatter:
    """
    Format application models into Telegram messages.
    """

    @staticmethod
    def format_product(
        product: Product,
    ) -> str:
        """
        Convert a Product into a Telegram message.

        Args:
            product:
                Product object.

        Returns:
            Formatted Telegram message.
        """

        return (
            "🔍 Product Found\n\n"
            f"📦 Product: {product.title}\n"
            f"🏪 Store: {product.store}\n"
            f"💰 Price: {product.price:,} Toman\n"
            f"🔗 URL: {product.url}"
        )