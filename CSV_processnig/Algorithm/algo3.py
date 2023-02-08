import pandas as pd

df = pd.read_csv("Dis_Tests.csv", index_col="disease")
df.fillna(0, inplace=True)
disease_inferred = "panic disorder"
d = df.loc[disease_inferred].tolist()
l = list(filter(lambda x: x != 0, d))
print(l)
