"""
product.py

Product data model.
"""

# ==========================================================
# Third-Party Imports
# ==========================================================

from pydantic import BaseModel
from pydantic import Field


class Product(BaseModel):
    """
    Product model.

    Represents a product found by a scraper.
    """

    # Product title.
    title: str = Field(
        ...,
        description="Product title",
    )

    # Store name.
    store: str = Field(
        ...,
        description="Store name",
    )

    # Product price.
    price: int = Field(
        ...,
        ge=0,
        description="Price in toman",
    )

    # Product URL.
    url: str = Field(
        default="",
        description="Product URL",
    )

    # Product image URL.
    image_url: str = Field(
        default="",
        description="Product image",
    )