"""
messages.py

Store every user-facing message used by the application.

This module contains only static text.

If a message requires dynamic values such as product
name, price or store, it should be formatted inside
message_formatter.py instead of this module.
"""

# ==========================================================
# Welcome Messages
# ==========================================================

WELCOME_MESSAGE = """
👋 <b>Welcome to Lanoo!</b>

Lanoo helps you compare product prices across multiple
online stores.

Simply send a product name using the command below:

<code>/price iPhone 15 Pro</code>

You can also type:

<code>/help</code>

to see all available commands.
"""

# ==========================================================
# Help Messages
# ==========================================================

HELP_MESSAGE = """
<b>Available Commands</b>

<b>/start</b>
Start the bot.

<b>/help</b>
Show this help message.

<b>/price &lt;product name&gt;</b>
Search for product prices.

Example:

<code>/price AirPods Pro 2</code>
"""

# ==========================================================
# Price Command Messages
# ==========================================================

PRICE_USAGE_MESSAGE = """
Please enter a product name.

Example:

<code>/price iPhone 15 Pro</code>
"""

SEARCHING_MESSAGE = """
🔎 Searching for the best prices...

Please wait...
"""

NO_PRODUCTS_FOUND_MESSAGE = """
❌ No products were found.

Try using a different product name.
"""

PRODUCTS_FOUND_MESSAGE = """
✅ Found <b>{count}</b> matching product(s).
"""

# ==========================================================
# Product Templates
# ==========================================================

PRODUCT_TEMPLATE = """
🛍 <b>{name}</b>

💰 Price: <b>{price}</b>

🏪 Store: <b>{store}</b>
"""

PRODUCT_LINK_TEMPLATE = """
🔗 {url}
"""

# ==========================================================
# Error Messages
# ==========================================================

UNKNOWN_COMMAND_MESSAGE = """
❌ Unknown command.

Type

<code>/help</code>

to see all available commands.
"""

UNEXPECTED_ERROR_MESSAGE = """
⚠️ Something went wrong.

Please try again later.
"""

NETWORK_ERROR_MESSAGE = """
🌐 Network error.

Please try again in a few minutes.
"""

TIMEOUT_ERROR_MESSAGE = """
⌛ The request timed out.

Please try again.
"""

# ==========================================================
# Validation Messages
# ==========================================================

EMPTY_PRODUCT_NAME_MESSAGE = """
Please enter a product name after the command.

Example:

<code>/price Coffee Maker</code>
"""

PRODUCT_NAME_TOO_LONG_MESSAGE = """
The product name is too long.

Please use a shorter search query.
"""

# ==========================================================
# Future Features
# ==========================================================

FEATURE_NOT_AVAILABLE_MESSAGE = """
🚧 This feature is not available yet.

It will be added in a future update.
"""