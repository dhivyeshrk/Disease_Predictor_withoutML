import pandas as pd

df = pd.read_csv("Med_Dis.csv", index_col="disease")
df.fillna(0, inplace=True)

d = df.loc['panic disorder'].tolist()
l = list(filter(lambda x: x != 0, d))
print(l)
