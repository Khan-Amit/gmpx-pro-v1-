import requests
import pandas as pd
from config import Config

# --- GOLD PRICE (Yahoo Finance fallback) ---
def get_gold_price():
    try:
        url = "https://query1.finance.yahoo.com/v7/finance/chart/GC=F"
        res = requests.get(url, timeout=10)
        data = res.json()

        price = data["chart"]["result"][0]["meta"]["regularMarketPrice"]
        return price

    except Exception:
        return None


# --- USD INDEX (DXY proxy via ETF UUP) ---
def get_usd_index():
    try:
        url = "https://query1.finance.yahoo.com/v7/finance/chart/UUP"
        res = requests.get(url, timeout=10)
        data = res.json()

        price = data["chart"]["result"][0]["meta"]["regularMarketPrice"]
        return price

    except Exception:
        return None


# --- VIX (Market Fear) ---
def get_vix():
    try:
        url = "https://query1.finance.yahoo.com/v7/finance/chart/^VIX"
        res = requests.get(url, timeout=10)
        data = res.json()

        price = data["chart"]["result"][0]["meta"]["regularMarketPrice"]
        return price

    except Exception:
        return None
