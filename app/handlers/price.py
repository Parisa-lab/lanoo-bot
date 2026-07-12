"""
price.py

Handle the /price command.
"""

from telegram import Update
from telegram.ext import ContextTypes

from app.messages import FEATURE_NOT_AVAILABLE_MESSAGE
from app.telegram import send_message


async def price_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    """
    Handle the /price command.

    This is a temporary implementation.
    The real price search will be added later.
    """

    _ = context

    await send_message(
        update=update,
        text=FEATURE_NOT_AVAILABLE_MESSAGE,
    )