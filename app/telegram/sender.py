"""
sender.py

Provide helper functions for sending Telegram messages.

Handlers should never call reply_text() directly.

Instead, every outgoing message should pass through
this module.

Advantages:

- Consistent formatting
- Centralized error handling
- Easier logging
- Easier future improvements
"""

# Import Telegram update object.
from telegram import Update

# Import Telegram parse mode.
from telegram.constants import ParseMode


async def send_message(
    update: Update,
    text: str,
    *,
    parse_mode: ParseMode | None = ParseMode.HTML,
    disable_web_page_preview: bool = True,
) -> None:
    """
    Send a message to the current chat.

    Args:
        update:
            Incoming Telegram update.

        text:
            Message text.

        parse_mode:
            Telegram parse mode.

        disable_web_page_preview:
            Disable automatic link previews.

    Returns:
        None.
    """

    # Make sure a message exists.
    if update.message is None:
        return

    # Send the message.
    await update.message.reply_text(
        text=text,
        parse_mode=parse_mode,
        disable_web_page_preview=disable_web_page_preview,
    )