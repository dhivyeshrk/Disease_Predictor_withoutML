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

with open("To_process.csv", "r", encoding="utf-8") as f:
    data = f.readlines()
# remove symptoms
result = []
for line in data:
    ind = line.find(']')
    temp = line[ind + 1:]
    result.append(temp + "\n")

writeFile("To_remove_newline.csv", result)
remove_newline("To_remove_newline.csv", "Symptoms_removed1.csv")

