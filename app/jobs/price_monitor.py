"""
Telegram job wrapper.
"""

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
):

    notification_service = (
        NotificationService(
            context.bot
        )
    )

    monitoring = MonitoringService(
        repository=repository,
        scraper=scraper,
        notifications=notification_service,
    )

    await monitoring.check_prices()