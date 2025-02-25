import matplotlib.pyplot as plt
from lgWorkflow import StockState

def plot_stock_data(inputs: StockState):
    data, ticker = inputs["data"], inputs["ticker"]
    fig, ax1 = plt.subplots(figsize=(10, 5))
    
    ax1.plot(data.index, data["Close"], label=f"{ticker} Closing Price (INR)", color="blue")
    ax1.set_xlabel("Date")
    ax1.set_ylabel("Price (INR)")
    
    if "SMA_50" in data.columns:
        ax1.plot(data.index, data["SMA_50"], label="50-day SMA", linestyle="dashed", color="green")
    if "SMA_200" in data.columns:
        ax1.plot(data.index, data["SMA_200"], label="200-day SMA", linestyle="dashed", color="red")
    
    ax1.legend()
    ax1.grid(True)
    
    # Create a second subplot for Volume Trend
    if "Volume_Trend" in data.columns:
        ax2 = ax1.twinx()
        ax2.plot(data.index, data["Volume_Trend"], label="Volume Trend", color="yellow", linestyle="dashed")
        ax2.set_ylabel("Volume")
        ax2.legend()
    
    plt.title(f"{ticker} Stock Price Trend")
    plt.show()
    return inputs