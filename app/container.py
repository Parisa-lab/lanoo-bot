"""
Dependency container.

Creates shared application services.
"""

from app.repositories.product_repository import ProductRepository
from app.scrapers import TorobScraper
from app.services.price_service import PriceService

repository = ProductRepository()

scraper = TorobScraper()

price_service = PriceService(
    scraper=scraper,
    repository=repository,
)