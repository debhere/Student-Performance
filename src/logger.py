import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%d_%b_%Y_%H_%M_%S')}.log"
LOG_DATE_FOLDER = f"{datetime.now().strftime('%d%m%y')}"
LOG_FOLDER = os.path.join(os.getcwd(), "logs", LOG_DATE_FOLDER)
os.makedirs(LOG_FOLDER, exist_ok=True)

LOG_FILE_PATH = os.path.join(os.getcwd(), LOG_FOLDER, LOG_FILE)

logging.basicConfig(
    filename = LOG_FILE_PATH,
    format = "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO
)