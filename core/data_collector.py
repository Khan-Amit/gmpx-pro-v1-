import time
from core.data_sources import get_gold_price, get_usd_index, get_vix
from core.logger import setup_logger

logger = setup_logger()


class DataCollector:

    def __init__(self):
        self.retry_limit = 3

    def fetch_with_retry(self, func, name):
        for _ in range(self.retry_limit):
            try:
                data = func()
                if data is not None:
                    return data
            except:
                pass
            time.sleep(1)
        return None

    def collect_all(self):
        data = {}

        data["gold_price"] = self.fetch_with_retry(get_gold_price, "gold")
        data["usd_index"] = self.fetch_with_retry(get_usd_index, "usd")
        data["vix"] = self.fetch_with_retry(get_vix, "vix")

        # Fallback values
        if data["gold_price"] is None:
            data["gold_price"] = 2000

        if data["usd_index"] is None:
            data["usd_index"] = 100

        if data["vix"] is None:
            data["vix"] = 20

        return data
