import csv
def remove_newline(read_file, write_file):
    with open(f"{read_file}", "r", newline='', encoding="utf-8") as in_file:
        with open(f"{write_file}", 'w', newline='', encoding="utf-8") as out_file:
            writer = csv.writer(out_file)
            for row in csv.reader(in_file):
                if row:
                    writer.writerow(row)


with open("Disease_List_Final.csv", "r", encoding="utf-8") as f:
    dis = f.readlines()

with open("newpercent.csv", "r", encoding="utf-8") as f:
    data = f.readlines()

# for line in data:
#     print(type(line))
print(type(data))

#
# fin = []
# for d in dis:
#     fin.append(d[:-1])
# dis = fin
# md = []
# lenMed= []
# for m in med:
#     ls = m.split(",")
#     lenMed.append(len(ls))
#     md.append(ls)
# res = []
# for ind, d in enumerate(dis):
#     md[ind].insert(0,d)
#     md[ind] = md[ind][:-1]
# # print(md)
# # print(max(lenMed))  # 17
# header = ["disease"]
# for i in range(max(lenMed)):
#     header.append(f"test{i+1}")
# # print(header)
# with open("Dis_Tests_temp.csv", "w", encoding="utf-8") as f:
#     writer = csv.writer(f)
#     writer.writerow(header)
#     writer.writerows(md)
#
# remove_newline("Dis_Tests_temp.csv", "Dis_Tests.csv")