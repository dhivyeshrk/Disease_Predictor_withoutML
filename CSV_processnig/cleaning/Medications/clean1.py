import csv
def remove_newline(read_file, write_file):
    with open(f"{read_file}", "r", newline='', encoding="utf-8") as in_file:
        with open(f"{write_file}", 'w', newline='', encoding="utf-8") as out_file:
            writer = csv.writer(out_file)
            for row in csv.reader(in_file):
                if row:
                    writer.writerow(row)

def writeFile(write_file, write_list):
    with open(f"{write_file}", "w", newline="\n", encoding="utf-8") as f:
        for res in write_list:
            f.write(res)

# with open("Remove_name.csv", "r", encoding="utf-8") as f:
#     data = f.readlines()
# result = []
# for line in data:
#     ind2 = line.find(']')
#     temp = line[ind2+2:]
#     result.append(temp)
# writeFile("To_process.csv", result)

with open("To_process.csv", "r", encoding="utf-8") as f:
    data = f.readlines()

# result = []
# for line in data:
#     start_ind = line.find('[')
#     end_ind = line.find(']')
#     temp = line[start_ind:end_ind+2]
#     result.append(temp + "\n")
# writeFile("To_process2.csv", result)

Medications = []
for ind,line in enumerate(data):
    indices = [i for i in range(len(line)) if line.startswith("commonMedications", i)]
    temp = []
    for i in indices:
        start_ind = i + len('commonMedications"":""')
        end_ind = line.find('"', start_ind)
        temp.append(line[start_ind:end_ind])
    Medications.append(temp)

with open("Med_temp.csv", "w", encoding="utf-8") as f:
    writer = csv.writer(f)
    for med in Medications:
        writer.writerow(med)

remove_newline("Med_temp.csv", "Medications_Drugs.csv")

