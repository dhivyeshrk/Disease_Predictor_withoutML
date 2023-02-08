import pandas as pd
import csv

with open("Diseases_Symptoms_test.csv", "r", newline='') as in_file:
    with open("Disease_and_Symptoms_final.csv", 'w', newline='') as out_file:
        writer = csv.writer(out_file)
        for row in csv.reader(in_file):
            if row:
                writer.writerow(row)