from core.data_collector import DataCollector
from core.feature_engine import FeatureEngine

from core.factor_engines.currency_engine import CurrencyEngine
from core.factor_engines.risk_engine import RiskEngine
from core.factor_engines.momentum_engine import MomentumEngine


def main():
    print("🚀 GMPX-PRO V1 Intelligence Running...")

    collector = DataCollector()
    raw_data = collector.collect_all()

    fe = FeatureEngine()
    features = fe.build_features(raw_data)

    currency = CurrencyEngine().compute(features)
    risk = RiskEngine().compute(features)
    momentum = MomentumEngine().compute(features)

    print("\n📊 FACTOR SCORES:")
    print("Currency:", currency)
    print("Risk:", risk)
    print("Momentum:", momentum)


if __name__ == "__main__":
    main()
