from core.data_collector import DataCollector
from core.feature_engine import FeatureEngine

from core.factor_engines.currency_engine import CurrencyEngine
from core.factor_engines.risk_engine import RiskEngine
from core.factor_engines.momentum_engine import MomentumEngine

from core.signal_engine import SignalEngine


def main():
    print("🚀 GMPX-PRO V1 Signal Engine Running...")

    collector = DataCollector()
    raw_data = collector.collect_all()

    fe = FeatureEngine()
    features = fe.build_features(raw_data)

    currency = CurrencyEngine().compute(features)
    risk = RiskEngine().compute(features)
    momentum = MomentumEngine().compute(features)

    signal_engine = SignalEngine()
    score = signal_engine.compute(currency, risk, momentum)
    decision = signal_engine.classify(score)

    print("\n📊 FACTORS:")
    print("Currency:", currency)
    print("Risk:", risk)
    print("Momentum:", momentum)

    print("\n🎯 FINAL SIGNAL:")
    print("Score:", score)
    print("Decision:", decision)


if __name__ == "__main__":
    main()
