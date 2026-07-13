"""
logger.py

Configure the application's logging system.

This module is responsible for:

- Configuring the root logger
- Creating colored console logs
- Creating rotating log files
- Preventing duplicate handlers
- Providing one centralized logging configuration
"""

# ==========================================================
# Standard Library Imports
# ==========================================================

# Import Python logging package.
#
# Every module inside the project should use logging
# instead of print().
import logging

# Import rotating file handler.
#
# Automatically creates backup log files when
# the current file reaches the maximum size.
from logging.handlers import RotatingFileHandler

# Import pathlib.
#
# Used for safe file system operations.
from pathlib import Path

# ==========================================================
# Third-Party Imports
# ==========================================================

# Import ColoredFormatter.
#
# This formatter adds colors to console output.
from colorlog import ColoredFormatter

# ==========================================================
# Local Imports
# ==========================================================

# Import application settings.
#
# Log level is read from configuration.
from app.config import settings

# ==========================================================
# Logger Constants
# ==========================================================

# Directory used for log files.
LOG_DIRECTORY = Path("logs")

# Main log file.
LOG_FILE = LOG_DIRECTORY / "lanoo.log"

# Maximum size of one log file.
#
# 5 MB
MAX_LOG_FILE_SIZE = 5 * 1024 * 1024

# Number of backup files.
BACKUP_COUNT = 5

# ==========================================================
# Helper Functions
# ==========================================================

def _create_log_directory() -> None:
    """
    Create the logs directory if it does not exist.

    Returns:
        None.
    """

    # Create the directory.
    #
    # exist_ok=True prevents raising an exception
    # if the directory already exists.
    LOG_DIRECTORY.mkdir(
        parents=True,
        exist_ok=True,
    )


def _build_console_formatter() -> ColoredFormatter:
    """
    Create the colored console formatter.

    Returns:
        ColoredFormatter.
    """

    return ColoredFormatter(

        # Log message format.
        "%(log_color)s"
        "%(levelname)-8s"
        "%(reset)s | "
        "%(blue)s"
        "%(name)s"
        "%(reset)s | "
        "%(cyan)s"
        "%(filename)s"
        "%(reset)s:"
        "%(lineno)d | "
        "%(message)s",

        # Color mapping.
        log_colors={

            "DEBUG": "cyan",

            "INFO": "green",

            "WARNING": "yellow",

            "ERROR": "red",

            "CRITICAL": "bold_red",

        },
    )


def _build_file_formatter() -> logging.Formatter:
    """
    Create the formatter used for log files.

    Returns:
        logging.Formatter.
    """

    return logging.Formatter(

        "%(asctime)s | "
        "%(levelname)-8s | "
        "%(name)s | "
        "%(filename)s:%(lineno)d | "
        "%(message)s"

    )

def _build_console_handler() -> logging.StreamHandler:
    """
    Create the console log handler.

    Returns:
        logging.StreamHandler.
    """

    # Create a console handler.
    console_handler = logging.StreamHandler()

    # Apply the colored formatter.
    console_handler.setFormatter(
        _build_console_formatter()
    )

    # Return the configured handler.
    return console_handler


def _build_file_handler() -> RotatingFileHandler:
    """
    Create the rotating file handler.

    Returns:
        RotatingFileHandler.
    """

    # Create the rotating log file handler.
    file_handler = RotatingFileHandler(
        filename=LOG_FILE,
        maxBytes=MAX_LOG_FILE_SIZE,
        backupCount=BACKUP_COUNT,
        encoding="utf-8",
    )

    # Apply the file formatter.
    file_handler.setFormatter(
        _build_file_formatter()
    )

    # Return the configured handler.
    return file_handler


# ==========================================================
# Public Functions
# ==========================================================

def setup_logging() -> None:
    """
    Configure the application's logging system.

    This function should only be called once during
    application startup.

    Returns:
        None.
    """

    # Get the root logger.
    root_logger = logging.getLogger()

    # Prevent duplicate handlers.
    #
    # Railway may import the application more than
    # once during deployment.
    if root_logger.handlers:
        return

    # Create the logs directory.
    _create_log_directory()

    # Set the logging level.
    root_logger.setLevel(
        settings.log_level,
    )

    # Create the console handler.
    console_handler = _build_console_handler()

    # Create the file handler.
    file_handler = _build_file_handler()

    # Register the console handler.
    root_logger.addHandler(
        console_handler,
    )

    # Register the file handler.
    root_logger.addHandler(
        file_handler,
    )

    # Prevent messages from propagating twice.
    root_logger.propagate = False

    # Write startup log.
    logging.getLogger(__name__).info(
        "========================================"
    )

    logging.getLogger(__name__).info(
        "Logging system initialized successfully."
    )

    logging.getLogger(__name__).info(
        "Log level: %s",
        logging.getLevelName(settings.log_level),
    )

    logging.getLogger(__name__).info(
        "Log file: %s",
        LOG_FILE.resolve(),
    )

    logging.getLogger(__name__).info(
        "========================================"
    )