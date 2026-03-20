import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    GOLD_API = os.getenv("API_KEY_GOLD")
    FRED_API = os.getenv("API_KEY_FRED")
    NEWS_API = os.getenv("API_KEY_NEWS")

    SECRET_KEY = os.getenv("SECRET_KEY")

    DATA_PATH = "data/raw/"
    LOG_PATH = "logs/"
