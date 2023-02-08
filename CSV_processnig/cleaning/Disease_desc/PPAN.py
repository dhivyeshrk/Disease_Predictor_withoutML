import csv
import pandas as pd
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

df = pd.read_csv("DIS_AND_DESC_FINAL.csv")

DISEASE = ["panic disorder", "depression"]

for ind,disease in enumerate(DISEASE):
    if ind>1:
        break
    df2 = df.loc[df['disease'] == disease]
    li = df2['desc'].tolist()
    print(li)


