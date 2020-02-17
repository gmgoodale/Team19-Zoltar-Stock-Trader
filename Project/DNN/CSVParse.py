import csv
import os
from pathlib import Path

CSVFILE = "test1.csv"
NEWFILE = "rando.csv"

if (not os.path.exists(NEWFILE)):
    Path(NEWFILE).touch()

with open(CSVFILE, newline='') as file:
    fileReader = csv.reader(file, delimiter=' ', quotechar='|')
    elements = [fileReader[x:x+100] for x in range(0, len(fileReader), 100)]

with open(NEWFILE, newline='') as newFile:
    newFile = csv.writer(newFile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    newFile.writerow(elements)
