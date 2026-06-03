import pandas as pd

df = pd.read_csv("../data/crypto.csv")
print(df.columns.tolist())