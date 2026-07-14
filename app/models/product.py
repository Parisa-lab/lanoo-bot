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
    """

    title: str = Field(
        ...,
        description="Product title",
    )

    store: str = Field(
        ...,
        description="Store name",
    )

    price: int = Field(
        ...,
        ge=0,
        description="Price in toman",
    )

    url: str = Field(
        default="",
        description="Product URL",
    )

    image_url: str = Field(
        default="",
        description="Product image URL",
    )