import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DATA_PATH = "data/raw/"
    LOG_PATH = "logs/"
    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret")
