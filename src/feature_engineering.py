import numpy as np

def create_features(df):
    # returns
    df['return'] = df['close'].pct_change()

    # target volatility
    df['volatility'] = df['return'].rolling(7).std()

    # moving averages
    df['ma7'] = df['close'].rolling(7).mean()
    df['ma21'] = df['close'].rolling(21).mean()

    # SAFE liquidity ratio (avoid division by zero)
    df['liquidity_ratio'] = df['volume'] / df['market_cap']

    # bollinger bands
    df['bb_mid'] = df['close'].rolling(20).mean()
    df['bb_std'] = df['close'].rolling(20).std()
    df['bb_upper'] = df['bb_mid'] + 2 * df['bb_std']
    df['bb_lower'] = df['bb_mid'] - 2 * df['bb_std']

    # ATR
    df['atr'] = (df['high'] - df['low']).rolling(14).mean()

    # 🔥 CRITICAL FIX
    df.replace([np.inf, -np.inf], np.nan, inplace=True)

    # Drop rows with NaN
    df = df.dropna()

    return df
