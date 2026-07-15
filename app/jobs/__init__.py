"""
Job registration.
"""

from app.jobs.price_monitor import check_prices


def register_jobs(application):

    application.job_queue.run_repeating(
        check_prices,
        interval=3600,   # 1 hour
        first=10,
    )