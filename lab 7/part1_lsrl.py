import math
import numpy as np
import csv

with open('part1_trial1.csv') as file:
    csvFile = csv.reader(file)
    for lines in csvFile:
        print(lines)