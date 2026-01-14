import pandas as pd

def apply_indicators(df: pd.DataFrame):
    # Safety Check: If DataFrame is empty or missing 'Close', return it as is
    if df.empty or 'Close' not in df.columns:
        print("Warning: Skipping indicators - No valid data found.")
        return df
        
    df['SMA_50'] = df['Close'].rolling(window=50).mean()
    df['SMA_200'] = df['Close'].rolling(window=200).mean()
    
    # RSI Calculation
    delta = df['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    df['RSI'] = 100 - (100 / (1 + rs))
    
    return df