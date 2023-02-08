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

with open("Symptoms_list.csv", "r", encoding="utf-8") as f:
    data = f.readlines()

result = []
for line in data:
    line = line.lower()
    result.append(line)

# with open("Symptoms_list_temp.csv", "w", encoding="utf-8") as f:
#     writer = csv.writer(f)
#     writer.writerows(result)
writeFile("Symptoms_list_temp.csv", result)
remove_newline("Symptoms_list_temp.csv", "Symptoms_list_2.csv")