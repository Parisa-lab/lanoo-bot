"""
price.py

Price command handler.
"""

from telegram import Update
from telegram.ext import ContextTypes

from app.telegram.sender import send_message


async def price_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    """
    Handle /price command.
    """

    await send_message(
        update,
        (
            "🔍 Price Search Result\n\n"
            "Product: iPhone 16 Pro\n"
            "Store: Test Store\n"
            "Price: 89,900,000 Toman\n\n"
            "✅ Handler works correctly."
        ),
    )