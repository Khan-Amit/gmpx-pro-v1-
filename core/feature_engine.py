class FeatureEngine:

    def normalize(self, value, min_val, max_val):
        return (value - min_val) / (max_val - min_val)

    def build_features(self, data):
        return {
            "gold_norm": self.normalize(data["gold_price"], 1500, 2500),
            "usd_norm": self.normalize(data["usd_index"], 90, 120),
            "vix_norm": self.normalize(data["vix"], 10, 50),
        }
