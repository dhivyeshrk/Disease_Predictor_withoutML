import csv

with open("Symptoms_removed1.csv", "r", encoding="utf-8") as f:
    data = f.readline()

result = []
for line in data:
    ind = line.find(',', 2)
    result.append(line[ind+1:] + "\n")

with open(".csv", "w", newline="\n", encoding="utf-8") as f:
    for line in result:
        f.write(line)

# removing newlines from result

with open("To_remove_newline.csv", "r", newline='', encoding="utf-8") as in_file:
    with open("Symptoms_removed1.csv", 'w', newline='', encoding="utf-8") as out_file:
        writer = csv.writer(out_file)
        for row in csv.reader(in_file):
            if row:
                writer.writerow(row)


