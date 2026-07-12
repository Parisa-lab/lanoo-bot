"""
logger.py

Configure the application's logging system.

Every module in the project should use Python's logging
module instead of print().

Features:

- Colored console output
- File logging
- Configurable log level
- Production-ready configuration
"""

# Import the logging module.
#
# This is Python's built-in logging framework.
import logging

# Import RotatingFileHandler.
#
# This handler automatically creates new log files
# when the current log file reaches its size limit.
from logging.handlers import RotatingFileHandler

# Import Path.
#
# Path provides a platform-independent way to work
# with file system paths.
from pathlib import Path

# Import ColoredFormatter.
#
# colorlog adds colors to console logs, making them
# easier to read during development.
from colorlog import ColoredFormatter

# Import application settings.
from app.config import settings


def setup_logging() -> None:
    """
    Configure the application's logging system.

    This function should be called only once when the
    application starts.

    Returns:
        None.
    """

    # Create the logs directory if it does not exist.
    log_directory = Path("logs")
    log_directory.mkdir(
        exist_ok=True,
    )

    # Create the root logger.
    logger = logging.getLogger()

    # Set the minimum logging level.
    logger.setLevel(
        settings.log_level,
    )

    # Prevent duplicate handlers if this function
    # is called more than once.
    if logger.handlers:
        return

    # ==========================================
    # Console Handler
    # ==========================================

    console_handler = logging.StreamHandler()

    console_formatter = ColoredFormatter(
        "%(log_color)s%(levelname)-8s%(reset)s | "
        "%(blue)s%(name)s%(reset)s | "
        "%(message)s",
        log_colors={
            "DEBUG": "cyan",
            "INFO": "green",
            "WARNING": "yellow",
            