import numpy as np

class FeatureEngine:

    def normalize(self, value, min_val, max_val):
        if value is None:
            return 0
        return (value - min_val) / (max_val - min_val)

    def build_features(self, data):
        features = {}

        # Normalize inputs
        features["gold_norm"] = self.normalize(data["gold_price"], 1500, 2500)
        features["usd_norm"] = self.normalize(data["usd_index"], 90, 120)
        features["vix_norm"] = self.normalize(data["vix"], 10, 50)

        return features
