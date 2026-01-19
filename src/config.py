import os
from dotenv import load_dotenv

load_dotenv()

# API Configurations
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

# Analysis Settings
DEFAULT_PERIOD = "1y"
CURRENCY_CONVERSION = True
BASE_CURRENCY = "USD"
TARGET_CURRENCY = "INR"

# Technical Parameters
SMA_SHORT = 50
SMA_LONG = 200
RSI_PERIOD = 14
RSI_OVERBOUGHT = 70
RSI_OVERSOLD = 30