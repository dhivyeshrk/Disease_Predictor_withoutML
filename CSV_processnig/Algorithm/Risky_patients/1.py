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

# remove_newline("risk.csv", "risk_2.csv")
# with open("risk.csv", "r", encoding="utf-8") as f:
#     data = f.readlines()

with open("Disease_List_Final.csv", "r", encoding="utf-8") as f:
    dis_list = f.readlines()

# result = []
# for line in data:
#     tem = line.lstrip()
#     result.append(tem + "\n")
#
# writeFile("risk_3_tem.csv", result)
# remove_newline("risk_3_tem.csv", "risk_3.csv")
with open("risk_3.csv", "r", encoding="utf-8") as f:
    data = f.readlines()
print(len(data))
print(len(dis_list))
header = ['disease']
for i in range(8):
    header.append(f"risk_age{i+1}")
vals = []
for i in range(len(dis_list)):
    vals.append(" ")

for ind,d in enumerate(data):
    tem,t3 = [],[]
    dis_list[ind] = dis_list[ind][:-1]
    tem.append(dis_list[ind])
    t2 = d.split(" , ")
    t2[-1] = t2[-1][:-2]
    print(t2)
    tem.extend(t2)
    vals[ind] = tem
print(vals)

with open("risk_4.csv", "w", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(vals)

remove_newline("risk_4.csv","risk_5.csv")
