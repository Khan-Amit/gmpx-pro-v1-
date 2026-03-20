import pandas as pd

class CorrelationEngine:

    def compute(self, series1, series2, window):
        return series1.rolling(window).corr(series2)

    def classify(self, value):
        if value is None:
            return "unknown"

        if value > 0.6:
            return "strong_positive"
        elif value > 0.2:
            return "mild_positive"
        elif value < -0.6:
            return "strong_negative"
        elif value < -0.2:
            return "mild_negative"
        else:
            return "neutral"
