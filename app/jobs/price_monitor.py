"""
app/jobs/price_monitor.py

Registers and executes the periodic
price monitoring job.
"""

from __future__ import annotations

from telegram.ext import Application

from app.container import repository
from app.container import scraper
from app.services.monitoring_service import (
    MonitoringService,
)
from app.services.notification_service import (
    NotificationService,
)


async def check_prices(
    context,
) -> None:
    """
    Executed by JobQueue.
    """

    notification_service = NotificationService(
        context.bot,
    )

    monitoring = MonitoringService(
        repository=repository,
        scraper=scraper,
        notifications=notification_service,
    )

    await monitoring.check_prices()


def register_price_monitor_job(
    application: Application,
) -> None:
    """
    Register recurring price monitor job.
    """

    application.job_queue.run_repeating(
        callback=check_prices,
        interval=300,  # every 5 minutes
        first=10,
        name="price_monitor",
    )