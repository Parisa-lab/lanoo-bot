"""
app/repositories/product_repository.py

Repository layer for tracked products.

Responsibilities:
- Create products
- Find products
- Load tracked products
- Update prices
- Create price history records

This file contains ONLY database access code.
No Telegram code.
No scraper code.
No business logic.
"""

from __future__ import annotations

from sqlalchemy import select

from app.database.models import PriceHistory
from app.database.models import TrackedProduct
from app.database.session import AsyncSessionLocal


class ProductRepository:
    """
    Repository for tracked products.
    """

    async def add_product(
        self,
        chat_id: int,
        url: str,
        title: str,
        price: str,
    ) -> TrackedProduct:
        """
        Create a new tracked product.
        """

        async with AsyncSessionLocal() as session:

            product = TrackedProduct(
                chat_id=chat_id,
                url=url,
                title=title,
                last_price=price,
            )

            session.add(product)

            await session.commit()
            await session.refresh(product)

            return product

    async def get_product_by_url(
        self,
        chat_id: int,
        url: str,
    ):
        """
        Find a tracked product by URL and chat.
        """

        async with AsyncSessionLocal() as session:

            result = await session.execute(
                select(TrackedProduct).where(
                    TrackedProduct.chat_id == chat_id,
                    TrackedProduct.url == url,
                )
            )

            return result.scalar_one_or_none()

    async def get_products_by_chat(
        self,
        chat_id: int,
    ):
        """
        Get all products tracked by a user.
        """

        async with AsyncSessionLocal() as session:

            result = await session.execute(
                select(TrackedProduct).where(
                    TrackedProduct.chat_id == chat_id
                )
            )

            return result.scalars().all()

    async def get_all_products(
        self,
    ):
        """
        Get every tracked product.
        Used by the monitoring job.
        """

        async with AsyncSessionLocal() as session:

            result = await session.execute(
                select(TrackedProduct)
            )

            return result.scalars().all()

    async def update_price(
        self,
        product_id: int,
        new_price: str,
    ) -> None:
        """
        Update product price and store
        a new price history record.
        """

        async with AsyncSessionLocal() as session:

            product = await session.get(
                TrackedProduct,
                product_id,
            )

            if not product:
                return

            product.last_price = new_price

            session.add(
                PriceHistory(
                    product_id=product.id,
                    price=new_price,
                )
            )

            await session.commit()