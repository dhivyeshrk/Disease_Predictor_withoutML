import csv

def readfile():
    with open("Symptoms_unprocessed.txt", encoding="utf-8") as f:
        return f.readlines()

data = readfile()  # max number of symptoms -> 24
all_symptoms, all_weights = [], []  # symptoms contains the unique symptoms over all diseases -> 377 in total
symptoms_index_ordered = []  # contains the symptoms of each disease which can be mapped to the disease using the index.
symptoms_and_weight = []
weights_index_ordered = []  # contains the weight of each symptom which can be mapped to the symptom using the index.
for disease_info in data:
    symptoms_indices = [i for i in range(len(disease_info)) if disease_info.startswith('""symptoms""', i)]
    symptom_temp, weight_temp, symptoms_and_weight_temp = [], [], []
    for ind, sym_index in enumerate(symptoms_indices):
        if ind % 2 == 0:  # symptom name
            symptom_start = sym_index + len('""symptoms"":""')
            symptom_end = disease_info.find('""', sym_index + len('"symptoms"":""'))
            symptom_name = disease_info[symptom_start: symptom_end]
            symptom_temp.append(symptom_name)
            if symptom_name not in all_symptoms:
                all_symptoms.append(symptom_name)  # To be the header of the csv file.
        else:
            weight_start = sym_index + len('""symptoms"":""')
            weight_end = disease_info.find('""', sym_index + len('""symptoms"":""'))
            weight_val = disease_info[weight_start:weight_end]
            weight_temp.append(weight_val)

            symptoms_and_weight_temp.append([symptom_name, weight_val])

    symptoms_index_ordered.append(symptom_temp)
    weights_index_ordered.append(weight_temp)
    symptoms_and_weight.append(symptoms_and_weight_temp)

with open("Disease_List.csv", "r") as f:
    diseases = f.readlines()

symptoms_file = all_symptoms.copy()
symptoms_file.insert(0, "Diseases")

with open("Diseases_Symptoms_test.csv", "w", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(symptoms_file)  # Header row
    for ind,dis in enumerate(diseases):
        file_write = []
        for symptom_check in all_symptoms:
            if symptom_check in symptoms_index_ordered[ind]:
                x = symptoms_index_ordered[ind].index(symptom_check)
                w = weights_index_ordered[ind][x]
                file_write.append(str(w))
            else:
                file_write.append(0)
        dis = dis[:len(dis)-1]
        file_write.insert(0,dis)
        print(file_write)
        writer.writerow(file_write)
