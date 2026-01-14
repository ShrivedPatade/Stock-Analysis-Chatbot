import pandas as pd

def generate_signals(state: dict):
    df = state['data']
    signals = []
    
    # Logic: Golden Cross (SMA 50 crosses above SMA 200)
    df['Prev_SMA_50'] = df['SMA_50'].shift(1)
    df['Prev_SMA_200'] = df['SMA_200'].shift(1)
    
    for i in range(1, len(df)):
        # Buy Signal: Golden Cross OR Oversold RSI
        if (df['SMA_50'].iloc[i] > df['SMA_200'].iloc[i] and 
            df['Prev_SMA_50'].iloc[i] <= df['Prev_SMA_200'].iloc[i]):
            signals.append({'date': df.index[i], 'type': 'BUY', 'price': df['Close'].iloc[i], 'reason': 'Golden Cross'})
            
        elif df['RSI'].iloc[i] < 30:
            signals.append({'date': df.index[i], 'type': 'BUY', 'price': df['Close'].iloc[i], 'reason': 'RSI Oversold'})

        # Sell Signal: Death Cross OR Overbought RSI
        if (df['SMA_50'].iloc[i] < df['SMA_200'].iloc[i] and 
            df['Prev_SMA_50'].iloc[i] >= df['Prev_SMA_200'].iloc[i]):
            signals.append({'date': df.index[i], 'type': 'SELL', 'price': df['Close'].iloc[i], 'reason': 'Death Cross'})
            
        elif df['RSI'].iloc[i] > 70:
            signals.append({'date': df.index[i], 'type': 'SELL', 'price': df['Close'].iloc[i], 'reason': 'RSI Overbought'})

    state['signals'] = signals
    return state