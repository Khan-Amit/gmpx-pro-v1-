import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


def get_gold_price():
    try:
        url = "https://query1.finance.yahoo.com/v8/finance/chart/GC=F"
        res = requests.get(url, headers=HEADERS, timeout=10)
        data = res.json()
        return data["chart"]["result"][0]["meta"]["regularMarketPrice"]
    except Exception as e:
        print("Gold error:", e)
        return None


def get_usd_index():
    try:
        url = "https://query1.finance.yahoo.com/v8/finance/chart/UUP"
        res = requests.get(url, headers=HEADERS, timeout=10)
        data = res.json()
        return data["chart"]["result"][0]["meta"]["regularMarketPrice"]
    except Exception as e:
        print("USD error:", e)
        return None


def get_vix():
    try:
        url = "https://query1.finance.yahoo.com/v8/finance/chart/^VIX"
        res = requests.get(url, headers=HEADERS, timeout=10)
        data = res.json()
        return data["chart"]["result"][0]["meta"]["regularMarketPrice"]
    except Exception as e:
        print("VIX error:", e)
        return None
