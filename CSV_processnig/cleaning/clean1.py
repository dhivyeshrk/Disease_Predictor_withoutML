import pandas as pd

def readfile():
    with open("csv_text.txt", encoding="utf-8") as f:
        return f.readlines()

file = readfile()  # list[str] #len(str) = 797
data = file
header = data[0]  # the heading of csv is removed
data.remove(header)

disease_index = []
symptoms = []  # array of values stored in the form of {"symptoms":"Leg pain"}. symptoms[0] will give symptoms for the first disease.
data_final = ""
for ind, line in enumerate(data):
    ind_pos = line.find(",")
    symptom_start, symptom_end = line.find("["), line.find("]")  # indices of symptoms
    str_int = (line[1:ind_pos] + "\n")  # index of disease
    data[ind] = str(line[ind_pos:])  # removing the disease code from main code
    symptoms.append(line[symptom_start + 1: symptom_end] + "\n")  # add symptom string to symptom list
    disease_index.append(str_int)  # add disease code to disease_index list

print(data.count("\n"))

with open("Symptoms_unprocessed.txt", encoding="utf-8", mode="w") as f:
    f.writelines(symptoms)
