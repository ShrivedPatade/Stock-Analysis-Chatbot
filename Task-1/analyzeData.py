from lgWorkflow import StockState
import pandas as pd

# Analyze stock data
def analyze_stock_data(inputs: StockState):
    data = inputs["data"]
    analysis_type = inputs.get("analysis_type", "basic")
    
    # if the analysis type is moving_average, calculate moving averages
    if "moving_average" in analysis_type:
        data = calculate_moving_averages(data)
    # if the analysis type is volume_trend, analyze volume trends
    if "volume_trend" in analysis_type:
        data = analyze_volume_trend(data)
    
    return {"data": data, "ticker": inputs["ticker"], "analysis_type": analysis_type}


# Function to calculate moving averages
def calculate_moving_averages(data: pd.DataFrame):
    data["SMA_50"] = data["Close"].rolling(window=50).mean()
    data["SMA_200"] = data["Close"].rolling(window=200).mean()
    return data

# Function to analyze volume trends
def analyze_volume_trend(data: pd.DataFrame):
    data["Volume_Trend"] = data["Volume"].rolling(window=7).mean()
    return data
