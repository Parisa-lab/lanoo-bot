"""
price.py

Price search command.
"""

from telegram import Update
from telegram.ext import ContextTypes

from app.telegram.sender import (
    send_message,
    send_warning_message,
)


async def price_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    """
    Handle /price command.
    """

    # User entered no search term.
    if not context.args:

        await send_warning_message(
            update,
            "Usage:\n/price product name",
        )

        return

    # Build search query.
    query = " ".join(
        context.args,
    )

    # Temporary output.
    await send_message(
        update,
        (
            "🔍 Search Request Received\n\n"
            f"Query: {query}\n\n"
            "Next step: PriceService"
        ),
    )