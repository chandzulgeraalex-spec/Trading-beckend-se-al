import pandas as pd
import numpy as np

def generate_signals(df):
    signals = []
    df['SMA10'] = df['close'].rolling(window=10).mean()
    df['SMA50'] = df['close'].rolling(window=50).mean()

    df['RSI'] = 100 - (100 / (1 + (df['close'].diff().clip(lower=0).rolling(14).mean() /
                                   df['close'].diff().clip(upper=0).abs().rolling(14).mean())))

    for i in range(1, len(df)):
        if df['SMA10'][i] > df['SMA50'][i] and df['RSI'][i] < 70:
            signals.append("buy")
        elif df['SMA10'][i] < df['SMA50'][i] and df['RSI'][i] > 30:
            signals.append("sell")
        else:
            signals.append("hold")

    df['signal'] = ['hold'] + signals
    return df['signal'].iloc[-1]
