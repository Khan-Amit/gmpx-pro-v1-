class CurrencyEngine:

    def compute(self, features):
        usd = features["usd_norm"]

        # Gold inverse relation
        score = 1 - usd

        return score
