"""
product.py

Define the Product model.

A Product object represents a single product returned
by a scraper.

Every scraper must return Product objects instead of
dictionaries.

Using a model provides:

- Better readability.
- Type safety.
- Easier maintenance.
- Better IDE support.
"""

# Import dataclass.
#
# A dataclass automatically generates useful methods
# such as __init__(), __repr__(), and __eq__().
from dataclasses import dataclass

# Import Optional.
#
# Optional means the value may be None.
from typing import Optional


@dataclass(slots=True)
class Product:
    """
    Represent a product.

    Every scraper should create and return Product
    instances.

    Attributes:
        name:
            Product name.

        price:
            Product price in the original currency.

        currency:
            Currency code.

        store:
            Store name.

        url:
            Product page URL.

        image_url:
            Product image URL.

        available:
            Whether the product is available.
    """

    # Product name.
    name: str

    # Product price.
    price: int

    # Currency code.
    currency: str

    # Store name.
    store: str

    # Product page URL.
    url: str

    # Product image.
    image_url: Optional[str] = None

    # Product availability.
    available: bool = True