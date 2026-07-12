"""
message_formatter.py

Build dynamic messages shown to users.

Unlike messages.py, which stores static text,
this module generates messages containing dynamic
data such as product names, prices, stores, and links.
"""

# Import message templates.
#
# All message templates are defined inside
# messages.py.
from app.messages import (
    PRODUCTS_FOUND_MESSAGE,
    PRODUCT_TEMPLATE,
    PRODUCT_LINK_TEMPLATE,
)


def build_products_found_message(
    count: int,
) -> str:
    """
    Build the message that tells the user how many
    products were found.

    Args:
        count:
            Number of matching products.

    Returns:
        A formatted message.
    """

    return PRODUCTS_FOUND_MESSAGE.format(
        count=count,
    )


def build_product_message(
    *,
    name: str,
    price: str,
    store: str,
) -> str:
    """
    Build a formatted product message.

    Args:
        name:
            Product name.

        price:
            Product price.

        store:
            Store name.

    Returns:
        A formatted product message.
    """

    return PRODUCT_TEMPLATE.format(
        name=name,
        price=price,
        store=store,
    )


def build_product_link_message(
    url: str,
) -> str:
    """
    Build a formatted product link.

    Args:
        url:
            Product URL.

    Returns:
        A formatted link message.
    """

    return PRODUCT_LINK_TEMPLATE.format(
        url=url,
    )