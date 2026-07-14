"""
price.py

Price search command handler.
"""

# ==========================================================
# Third-Party Imports
# ==========================================================

from telegram import Update
from telegram.ext import ContextTypes

# ==========================================================
# Local Imports
# ==========================================================

from app.services import PriceService

from app.telegram.sender import (
    send_message,
    send_warning_message,
)

# ==========================================================
# Command Handler
# ==========================================================

async def price_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    """
    Handle the /price command.

    Examples:

        /price iphone 16

        /price samsung s25 ultra

    Args:
        update:
            Telegram update.

        context:
            Telegram callback context.

    Returns:
        None.
    """

    # ------------------------------------------------------
    # Validate user input.
    # ------------------------------------------------------

    if not context.args:

        await send_warning_message(
            update,
            (
                "Usage:\n"
                "/price product name"
            ),
        )

        return

    # ------------------------------------------------------
    # Build search query.
    # ------------------------------------------------------

    query = " ".join(
        context.args,
    )

    # ------------------------------------------------------
    # Create service instance.
    # ------------------------------------------------------

    service = PriceService()

    # ------------------------------------------------------
    # Execute search.
    # ------------------------------------------------------

    result = await service.search(
        query,
    )

    # ------------------------------------------------------
    # Send result to the user.
    # ------------------------------------------------------

    await send_message(
        update,
        result,
    )