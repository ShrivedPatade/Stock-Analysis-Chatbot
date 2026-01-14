import yfinance as yf
import pandas as pd
import requests
from config import TARGET_CURRENCY

def fetch_stock_data(state: dict):
    """
    Fetches historical stock data and handles currency conversion.
    """
    ticker = state["ticker"]
    period = state["period"]
    
    try:
        print(f"Fetching data for {ticker}...")
        
        # FIXED: Removed the manual 'session' parameter to avoid conflicts with 
        # yfinance's internal scraper requirements.
        stock = yf.Ticker(ticker)
        df = stock.history(period=period)
        
        if df.empty:
            print(f"Warning: No data found for {ticker}. It may be invalid or delisted.")
            return {**state, "data": pd.DataFrame()}

        # Currency Conversion to INR
        if TARGET_CURRENCY == "INR":
            try:
                url = 'https://api.exchangerate-api.com/v4/latest/USD'
                rate = requests.get(url).json()['rates']['INR']
                df[["Open", "High", "Low", "Close"]] *= rate
            except Exception as e:
                print(f"Currency conversion skipped: {e}")
            
        return {**state, "data": df}

    except Exception as e:
        print(f"Fetch failed: {e}")
        return {**state, "data": pd.DataFrame()}