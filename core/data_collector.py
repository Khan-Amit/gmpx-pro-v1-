def collect_all(self):
    dataset = {}

    dataset["gold_price"] = self.fetch_with_retry(get_gold_price, "Gold")
    dataset["usd_index"] = self.fetch_with_retry(get_usd_index, "USD Index")
    dataset["vix"] = self.fetch_with_retry(get_vix, "VIX")

    # ✅ FALLBACK VALUES (CRITICAL)
    if dataset["gold_price"] is None:
        dataset["gold_price"] = 2000

    if dataset["usd_index"] is None:
        dataset["usd_index"] = 100

    if dataset["vix"] is None:
        dataset["vix"] = 20

    return dataset
