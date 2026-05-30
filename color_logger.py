from __future__ import annotations
import logging
import sys
from colorama import init, Fore, Style

# Enable ANSI colors on Windows
init(autoreset=True)

class ColorFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        level = record.levelno

        if level >= logging.ERROR:
            color = Fore.RED
        elif level >= logging.WARNING:
            color = Fore.YELLOW
        elif level >= logging.INFO:
            color = Fore.BLUE
        else:
            color = Fore.CYAN

        msg = super().format(record)
        return f"{color}{msg}{Style.RESET_ALL}"

# Create logger
def create_logger(name: str, clear_handlers: bool = True, default_level: int = logging.DEBUG) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(default_level)

    # Create console handler with color formatter
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(default_level)
    ch.setFormatter(ColorFormatter("%(asctime)s [%(levelname)s] %(message)s"))

    if clear_handlers:
        logger.handlers.clear()

    logger.addHandler(ch)
    return logger