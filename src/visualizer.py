import matplotlib.pyplot as plt

def plot_prediction(state: dict):
    df = state['data']
    signals = state.get('signals', [])
    ticker = state['ticker']
    
    if df.empty or 'Close' not in df.columns:
        print(f"Result: Could not generate visualization for {ticker} due to missing data.")
        return state
    
    # Create subplots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10), sharex=True, gridspec_kw={'height_ratios': [3, 1]})
    
    # Price and Averages
    ax1.plot(df.index, df['Close'], label='Close Price', alpha=0.6)
    ax1.plot(df.index, df['SMA_50'], label='50-day SMA', linestyle='--')
    ax1.plot(df.index, df['SMA_200'], label='200-day SMA', linestyle='--')
    
    # Plot Buy/Sell Markers
    for sig in signals:
        color = 'green' if sig['type'] == 'BUY' else 'red'
        marker = '^' if sig['type'] == 'BUY' else 'v'
        ax1.scatter(sig['date'], sig['price'], color=color, marker=marker, s=150, edgecolors='black', zorder=5)
    
    ax1.set_title(f"Predictive Analysis for {ticker}")
    ax1.legend()
    
    # RSI Subplot
    ax2.plot(df.index, df['RSI'], color='purple', label='RSI')
    ax2.axhline(70, color='red', linestyle=':', alpha=0.5)
    ax2.axhline(30, color='green', linestyle=':', alpha=0.5)
    ax2.set_ylabel('RSI')
    
    plt.title(f"Predictive Analysis: {ticker}")
    plt.tight_layout()
    plt.show()
    return state