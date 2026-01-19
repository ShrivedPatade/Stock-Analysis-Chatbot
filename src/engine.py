import pandas as pd

def generate_signals(state: dict):
    df = state['data']
    sentiment = state.get('sentiment', 0.0)
    signals = []
    
    # SAFETY CHECK: If the fetch or indicators failed, exit gracefully
    if df.empty or 'SMA_50' not in df.columns:
        print("Engine Warning: Missing technical data. Cannot generate signals.")
        state['signals'] = []
        state['recommendation'] = "DATA UNAVAILABLE"
        return state
    
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
    
    # FINAL ACTION LOGIC: Decision Filtering
    latest_close = df['Close'].iloc[-1]
    
    # Profit Maximization Strategy:
    # 1. If Sentiment is very strong (> 0.5), it can trigger a BUY even without a Golden Cross.
    # 2. If Technical is BUY but Sentiment is negative (< -0.3), we might downgrade to HOLD to avoid risk.
    
    recommendation = "HOLD"
    
    if signals:
        latest_signal = signals[-1]['type']
        
        # Maximize Profit with News Confirmation
        if latest_signal == 'BUY' and sentiment > 0.2:
            recommendation = "STRONG BUY (Technical + Positive News)"
        elif latest_signal == 'BUY' and sentiment < -0.2:
            recommendation = "HOLD (Technical Buy but Negative News Risk)"
        elif latest_signal == 'SELL' and sentiment < -0.2:
            recommendation = "STRONG SELL (Technical + Negative News)"
        elif latest_signal == 'SELL' and sentiment > 0.2:
            recommendation = "HOLD (Technical Sell but Positive News Momentum)"
    
    # Catch-all for extreme news shifts
    if sentiment > 0.6: recommendation = "BUY (Extreme Bullish Sentiment)"
    if sentiment < -0.6: recommendation = "SELL (Extreme Bearish Sentiment)"

    state['signals'] = signals
    state['recommendation'] = recommendation
    return state