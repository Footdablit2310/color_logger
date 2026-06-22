import logging

DEBUG = logging.DEBUG
INFO = logging.INFO
WARNING = logging.WARNING
WARN = logging.WARN
ERROR = logging.ERROR
ERR = logging.ERROR
CRITICAL = logging.CRITICAL
FATAL = logging.FATAL

def create_logger(name: str, clear_handlers: bool = True, default_level: int = logging.DEBUG) -> logging.Logger:
    """Creates a colored logger with the specified name and configuration."""