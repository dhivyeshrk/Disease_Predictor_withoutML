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

# def readFile(read_file, var):

# with open("Symptoms_removed1.csv", "r", encoding="utf-8") as f:
#     data = f.readlines()
# result = []
# for line in data:
#     ind = line.find(',',2)
#     temp = line[ind+1:]
#     result.append(temp)
#
# writeFile("Remove_name_temp.csv", result)
# remove_newline("Remove_name_temp.csv", "Remove_name.csv")

# with open("Remove_name.csv", "r", encoding="utf-8") as f:
#     data = f.readlines()
# result = []
#
# for line in data:
#     ind = line.find("Patients with")
#     result.append(line[:ind] + "\n")
#
# writeFile("Dis_desc_temp.csv", result)
# remove_newline("Dis_desc_temp.csv", "Dis_desc.csv")

with open("Dis_desc.csv", "r", encoding="utf-8") as f:
    data = f.readlines()
result = []

for line in data:
    s = list(line)
    for ind, char in enumerate(s):
        if ind + 1 < len(s):
            if char == ",":
                for i in range(ind, len(s)-1):
                    if s[i].isalpha():
                        break
                    if not s[i].isalpha():
                        del s[i]

    if s[len(s)-1] == ',':
        del s[len(s)-1]
    if s[1] == ',':
        s[1] = ""
    if s[0] == " " or s[0] == "  ":
        s[0] = ""
    s = filter(lambda x: x != '"', s)
    s = filter(lambda x: x != '  ', s)
    temp = ""
    for c in s:
        temp += c
    result.append(temp)

writeFile("Dis_comma_rem1_temp.csv",result)
remove_newline("Dis_comma_rem1_temp.csv", "DISEASES_DESCRIPTION.csv")


