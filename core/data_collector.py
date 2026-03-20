import time
from core.data_sources import get_gold_price, get_usd_index, get_vix
from core.logger import setup_logger

logger = setup_logger()


class DataCollector:

    def __init__(self):
        self.retry_limit = 3

    def fetch_with_retry(self, func, name):
        for attempt in range(self.retry_limit):
            try:
                data = func()
                if data is not None:
                    logger.info(f"{name} fetched: {data}")
                    return data
            except Exception as e:
                logger.error(f"{name} error: {e}")

            time.sleep(2)

        logger.warning(f"{name} failed after retries")
        return None

    def collect_all(self):
        dataset = {}

        dataset["gold_price"] = self.fetch_with_retry(get_gold_price, "Gold")
        dataset["usd_index"] = self.fetch_with_retry(get_usd_index, "USD Index")
        dataset["vix"] = self.fetch_with_retry(get_vix, "VIX")

        return dataset
