"""
Job registration.
"""

from app.jobs.price_monitor import monitor_price


def register_jobs(application):
    """
    Register scheduled jobs.
    """

    application.job_queue.run_repeating(
        monitor_price,
        interval=60,
        first=10,
    )