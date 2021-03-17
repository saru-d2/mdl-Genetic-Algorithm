import json  
import csv
import pandas as pd


with open('MAR15SUB.json', 'r') as fd:
    DATA = json.load(fd)

print(type(DATA))

with open('gen3.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for genNo, gen in enumerate(DATA['PrevGens']):
        # print(genNo)
        if genNo == 2:
            for cat in gen:
                # per category
                writer.writerow(str(cat))
                for i in range(11):
                    row = []
                    for vector in gen[cat]:
                        row.append(vector[i])
                    writer.writerow(row)
            if genNo > 2:
                break
                        

