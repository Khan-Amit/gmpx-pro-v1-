from core.data_collector import DataCollector

def main():
    print("🚀 GMPX-PRO V1 Running Data Collector...")

    collector = DataCollector()
    data = collector.collect_all()

    print("📊 Market Data:")
    print(data)

if __name__ == "__main__":
    main()
