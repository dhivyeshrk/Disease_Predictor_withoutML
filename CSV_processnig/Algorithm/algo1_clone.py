import pandas as pd
import time

start = time.time()
with open("Symptoms_list.csv", "r", encoding="utf-8") as f:
    Symptom_list = f.readlines()
res = []
for sy in Symptom_list:
    res.append(sy[:len(sy) - 1])

Symptom_list = res
Symptom_list = set(Symptom_list)
df = pd.read_csv("Diseases_and_Symptoms_final.csv")
tem = df.copy()
head_df = df.head()
symptoms = ["depression", "sharp chest pain", "irregular breathing"]
test = df.groupby(['diseases'])

# print(symptoms)
df["sum"] = df[symptoms].sum(axis=1)
# except Exception:
#     pass
t = df.groupby(['sum'], sort=True)
s = df.nlargest(10, "sum").sort_values('sum', ascending=False)
min_df = s
most_df = s

while min_df['sum'].std() >= 5:
    min_df = min_df[:-1]
most_df = min_df
while most_df['sum'].std() >= 2:
    most_df = most_df[:-1]

most_probable_dis = most_df['diseases'].to_numpy()
less_probable_dis = [i for i in min_df['diseases'].to_numpy() if i not in most_probable_dis]

print(f"Most probable diseases : {most_probable_dis}")
print(f"Less probable disease : {less_probable_dis}")

#  DRUGS EXTRACTION
df = pd.read_csv("Med_Dis.csv", index_col="disease")
df.fillna(0, inplace=True)
Medications = {}

for disease in most_probable_dis:
    d = df.loc[disease].tolist()
    med_temp = list(filter(lambda x: x != 0, d))
    Medications[disease] = med_temp
print(Medications)

print()

#  TESTS AND PROCEDURES EXTRACTION
df = pd.read_csv("Dis_Tests.csv", index_col="disease")
df.fillna(0, inplace=True)
Tests_Procedures = {}

for disease in most_probable_dis:
    d = df.loc[disease].tolist()
    t_p = list(filter(lambda x: x != 0, d))
    Tests_Procedures[disease] = t_p
print(Tests_Procedures)

end = time.time()
print(end-start)