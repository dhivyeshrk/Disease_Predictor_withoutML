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

with open("DISEASES_DESCRIPTION.csv", "r", encoding="utf-8") as f:
    data = f.readlines()

with open("Disease_List_Final.csv", "r", encoding="utf-8") as f:
    dis_list = f.readlines()

result = []
t2 = []
for i in range(len(dis_list)):
    t2.append(" ")
for ind,dis in enumerate(dis_list):
    temp = []
    dis = dis[:-1]
    data[ind] = data[ind][:-1]
    temp.append(dis)
    temp.append(data[ind])
    t2[ind] = temp

print(t2[0])

with open("Dis_and_desc.csv", "w", encoding="utf-8") as f:
    writer = csv.writer(f)
    header = ['disease', 'desc']
    writer.writerow(header)
    writer.writerows(t2)

remove_newline("Dis_and_desc.csv", "DIS_AND_DESC_FINAL.csv")

