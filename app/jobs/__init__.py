"""
Job package exports.

Author: Lanoo
"""

from app.jobs.price_monitor import check_prices

__all__ = [
    "check_prices",
]