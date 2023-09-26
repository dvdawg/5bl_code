import math
import numpy as np
import csv
import os

here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'part1_trial1.csv')

with open(filename) as file:
    csvFile = csv.reader(file)
    for lines in csvFile:
        print(lines)