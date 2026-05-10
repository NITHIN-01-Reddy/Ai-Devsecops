import logging
from pythonjsonlogger.json import JsonFormatter
import os

LOG_DIR = "logs"

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

logger = logging.getLogger("ai-devsecops")

logger.setLevel(logging.INFO)

logHandler = logging.FileHandler(f"{LOG_DIR}/app.log")

formatter = JsonFormatter(
    '%(asctime)s %(levelname)s %(name)s %(message)s'
)

logHandler.setFormatter(formatter)

logger.addHandler(logHandler)