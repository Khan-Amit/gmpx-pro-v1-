import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}


# --- GOLD PRICE (GC=F) ---
def get_gold_price():
    try:
        url = "https://query1.finance.yahoo.com/v8/finance/chart/GC=F"
        res = requests.get(url, headers=HEADERS, timeout=10)
        data = res.json()

        price = data["chart"]["result"][0]["meta"]["regularMarketPrice"]
        return price

    except Exception as e:
        print("❌ Gold fetch error:", e)
        return None


# --- USD INDEX (UUP ETF proxy) ---
def get_usd_index():
    try:
        url = "https://query1.finance.yahoo.com/v8/finance/chart/UUP"
        res = requests.get(url, headers=HEADERS, timeout=10)
        data = res.json()

        price = data["chart"]["result"][0]["meta"]["regularMarketPrice"]
        return price

    except Exception as e:
        print("❌ USD fetch error:", e)
        return None


# --- VIX (Fear Index) ---
def get_vix():
    try:
        url = "https://query1.finance.yahoo.com/v8/finance/chart/^VIX"
        res = requests.get(url, headers=HEADERS, timeout=10)
        data = res.json()

        price = data["chart"]["result"][0]["meta"]["regularMarketPrice"]
        return price

    except Exception as e:
        print("❌ VIX fetch error:", e)
        return None
