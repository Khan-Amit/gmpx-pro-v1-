import logging
import os
from config import Config

def setup_logger():
    os.makedirs(Config.LOG_PATH, exist_ok=True)

    logging.basicConfig(
        filename=os.path.join(Config.LOG_PATH, "gmpx.log"),
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    return logging.getLogger()
