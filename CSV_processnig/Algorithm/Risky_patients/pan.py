import pandas as pd

df = pd.read_csv("risk_5.csv")
df.fillna(0,inplace=True)

n_df = df.iloc[[0]]
# n_df = n_df.groupby(['disease'])

print(n_df['panic disorder'])