def readfile():
    with open("result2.txt", encoding="utf-8") as f:
        return f.readlines()


data = readfile()
diseases = []
for line in data:
    disease_start, disease_end = line.find(','), line.find(',', 2)
    disease_name = line[disease_start + 1:disease_end]
    diseases.append(disease_name + "\n")

for ind,dis in enumerate(diseases):
    if dis == "\n":
        del diseases[ind]

with open("Disease_List.csv", "w+", newline='\n') as f:
    for dis in diseases:
        f.write(dis)
    data = f.readlines()
print(data)
# for line in data:
#     if line == "\n":
#         del line
