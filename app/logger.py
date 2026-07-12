"""
logger.py

Configure the application's logging system.
"""

import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

from colorlog import ColoredFormatter

from app.config import settings


def setup_logging() -> None:
    """
    Configure application logging.
    """

    logger = logging.getLogger()

    # Prevent duplicate handlers.
    if logger.handlers:
        return

    logger.setLevel(settings.log_level)

    # Create logs directory.
    log_directory = Path("logs")
    log_directory.mkdir(exist_ok=True)

    # ----------------------------
    # Console Handler
    # ----------------------------

    console_handler = logging.StreamHandler()

    console_formatter = ColoredFormatter(
        "%(log_color)s%(levelname)-8s%(reset)s | "
       "%(blue)s%(name)s%(reset)s | "
       "%(message)s",
        log_colors={
            "DEBUG": "cyan",
            "INFO": "green",
            "WARNING": "yellow",
            "ERROR": "red",
            "CRITICAL": "bold_red",
        },
    )

    console_handler.setFormatter(console_formatter)

    # ----------------------------
    # File Handler
    # ----------------------------

    file_handler = RotatingFileHandler(
        filename=log_directory / "lanoo.log",
        maxBytes=5 * 1024 * 1024,
        backupCount=5,
        encoding="utf-8",
    )

    file_formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    file_handler.setFormatter(file_formatter)

    # ----------------------------
    # Register handlers
    # ----------------------------

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    logger.info("Logging system initialized successfully.")