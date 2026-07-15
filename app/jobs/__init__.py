"""
Job registration.
"""

from app.jobs.price_monitor import monitor_price


def register_jobs(application):

    application.job_queue.run_repeating(
        monitor_price,
        interval=10,
        first=10,
    )