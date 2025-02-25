import yfinance as yf
import requests
from lgWorkflow import StockState

# Fetch exchange rates (Open Exchange Rates API)
url = 'https://api.exchangerate-api.com/v4/latest/USD'
response = requests.get(url).json()
usd_to_local = response['rates']['INR'] 

# Fetch Stock data from Yahoo Finance, yfinance tool
def fetch_stock_data(inputs: StockState):
    ticker = inputs.get("ticker", "AAPL")
    period = inputs.get("period", "6mo")
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    
    # Convert to INR
    data[["Open", "High", "Low", "Close"]] *= usd_to_local
    
    return {"data": data, "ticker": ticker, "analysis_type": inputs.get("analysis_type", ["basic"])}