class SignalEngine:

    def compute(self, currency, risk, momentum):
        # weights (can tune later)
        score = (
            0.4 * currency +
            0.3 * risk +
            0.3 * momentum
        )

        return score

    def classify(self, score):
        if score > 0.65:
            return "STRONG BUY"
        elif score > 0.55:
            return "BUY"
        elif score < 0.35:
            return "STRONG SELL"
        elif score < 0.45:
            return "SELL"
        else:
            return "HOLD"
