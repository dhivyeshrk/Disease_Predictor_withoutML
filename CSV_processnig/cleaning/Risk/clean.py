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

# with open("To_process.csv", "r+", encoding="utf-8") as f:
#     data = f.readlines()
# result = []
# for line in data:
#     ind = line.find(']')
#     temp = line[ind+2:]
#     result.append(temp + "\n")
# writeFile("To_process2_temp.csv", result)
# remove_newline("To_process2_temp.csv", "To_process2.csv")

# with open("To_process2.csv", "r", encoding="utf-8") as f:
#     data = f.readlines()
# result = []
# for line in data:
#     ind = line.find(',')
#     temp = line[ind:]
#     result.append(temp + "\n")
#
# writeFile("To_process2.csv", result)
# remove_newline("To_process2.csv", "To_process2_fin.csv")

with open("To_process2_fin.csv", "r", encoding="utf-8") as f:
    data = f.readlines()
result = []
not_at_risk_age = []
for line in data:
    not_risk, symptom_dis = line.find("On the other hand"), line.find("Within all the people")
    if not_risk>0:
        stop_ind = line.find(".", not_risk)
        age_ind = [i for i in range(stop_ind) if line.startswith("age", i, stop_ind)]
        for l_ind in age_ind:
            age = line[l_ind+3:line.find("years", l_ind)]
            print(age)
    # if symptom_dis>0:
        # extract distribution of symptoms

