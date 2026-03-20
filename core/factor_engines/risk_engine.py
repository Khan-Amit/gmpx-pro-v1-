class RiskEngine:

    def compute(self, features):
        vix = features["vix_norm"]

        return vix  # higher VIX → bullish gold
