import logging

from telegram import Update
from telegram.ext import ContextTypes

logger = logging.getLogger(__name__)


async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:

    logger.info(
        f"/start received from user: {update.effective_user.id}"
    )

    await update.message.reply_text(
        "Welcome to Lanoo Bot."
    )