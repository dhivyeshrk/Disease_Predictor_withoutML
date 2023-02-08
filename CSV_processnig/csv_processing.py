import pandas as pd

df = pd.read_csv("C:\\Users\\DELL\\PycharmProjects\\Python_project_ICS_214\\disease_and_symptoms.csv", on_bad_lines=False)
print(df.head())
