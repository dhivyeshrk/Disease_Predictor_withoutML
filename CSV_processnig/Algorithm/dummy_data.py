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

# with open("Disease_List.csv", "r", encoding="utf-8") as f:
#     data = f.readlines()
#
# result = []
# for line in data:
#     result.append(line.lower() + "\n")
# print(result)
#
# writeFile("Disease_List_Temp.csv", result)
# remove_newline("Disease_List_Temp.csv", "Disease_List_Final.csv")

with open("Disease_and_Symptoms_final.csv", "r", encoding="utf-8") as f:
    data = f.readlines()

result = []
for line in data:
    result.append(line.lower() + "\n")
print(result)

writeFile("Disease_Symptom_Temp.csv", result)
remove_newline("Disease_Symptom_Temp.csv", "Diseases_and_Symptoms_final.csv")


