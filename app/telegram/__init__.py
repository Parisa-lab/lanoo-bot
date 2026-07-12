"""
telegram package

This package contains Telegram-specific functionality.

Modules in this package communicate directly with
the Telegram Bot API.
"""

from .sender import send_message

__all__ = [
    "send_message",
]