import pandas as pd
from sklearn.preprocessing import StandardScaler


def load_and_clean(path):
    df = pd.read_csv(path)

    # Standardize column names
    df.columns = df.columns.str.lower().str.strip()

    # Rename marketCap → market_cap
    if "marketcap" in df.columns:
        df.rename(columns={"marketcap": "market_cap"}, inplace=True)

    # Convert date if exists
    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors="coerce")

    # Forward fill missing values
    df = df.ffill()

    return df


def scale_features(df, cols):
    scaler = StandardScaler()
    df[cols] = scaler.fit_transform(df[cols])
    return df, scaler
