"""
app/repositories/product_repository.py

Repository for tracked products.

Responsibilities:
- Database access
- Product persistence
- Product retrieval
- Price updates

Business logic does NOT belong here.
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