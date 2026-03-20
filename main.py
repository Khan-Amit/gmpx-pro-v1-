from core.data_collector import DataCollector
from core.feature_engine import FeatureEngine

from core.factor_engines.currency_engine import CurrencyEngine
from core.factor_engines.risk_engine import RiskEngine
from core.factor_engines.momentum_engine import MomentumEngine

from core.signal_engine import SignalEngine


def main():
    print("🚀 GMPX-PRO V1 Running...\n")

    # Step 1: Collect Data
    collector = DataCollector()
    raw_data = collector.collect_all()

    print("🧪 RAW DATA:", raw_data)

    # Step 2: Build Features
    fe = FeatureEngine()
    features = fe.build_features(raw_data)

    # Step 3: Factor Engines
    currency = CurrencyEngine().compute(features)
    risk = RiskEngine().compute(features)
    momentum = MomentumEngine().compute(features)

    # Step 4: Signal
    signal_engine = SignalEngine()
    score = signal_engine.compute(currency, risk, momentum)
    decision = signal_engine.classify(score)

    # Output
    print("\n📊 FACTORS:")
    print("Currency:", round(currency, 3))
    print("Risk:", round(risk, 3))
    print("Momentum:", round(momentum, 3))

    print("\n🎯 FINAL SIGNAL:")
    print("Score:", round(score, 3))
    print("Decision:", decision)


if __name__ == "__main__":
    main()
