import re
import csv

with open("log.csv") as file:
    reader = csv.reader(file)
    for line, row in enumerate(reader):
        if line > 0:
            text = row[0]
            print(text)
            attr = re.search(r".*Method\:\s([A-Z])+|\n.*(http.*)",text)

            #print("at1",attr.group(1))
