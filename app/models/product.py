"""
product.py

Define the Product model.

Every scraper must return Product objects.

Never use dictionaries to represent products.
"""

from typing import Optional

from pydantic import Field
from pydantic import HttpUrl

from app.models.base import BaseSchema


class Product(BaseSchema):
    """
    Represent a product.
    """

    # Product name.
    name: str = Field(
        min_length=1,
        max_length=200,
    )

    # Product price.
    #
    # Always stored as an integer.
    price: int = Field(
        ge=0,
    )

    # Currency code.
    currency: str = Field(
        min_length=3,
        max_length=10,
    )

    # Store name.
    store: str = Field(
        min_length=1,
        max_length=100,
    )

    # Product page.
    url: HttpUrl

    # Optional image.
    image_url: Optional[HttpUrl] = None

    # Product availability.
    available: bool = True