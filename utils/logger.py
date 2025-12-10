import logging
import os
from logging.handlers import RotatingFileHandler

# Create logs directory if it doesn't exist
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, "test.log")

logger = logging.getLogger("framework")
logger.setLevel(logging.INFO)

# ------- Console Handler -------
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# ------- File Handler (Rotating) -------
file_handler = RotatingFileHandler(
    LOG_FILE, 
    maxBytes=2_000_000,  # 2 MB
    backupCount=3        # Keep last 3 logs
)
file_handler.setLevel(logging.INFO)

# ------- Formatter -------
formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# ------- Add handlers -------
if not logger.handlers:  # avoid duplicate logs
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
