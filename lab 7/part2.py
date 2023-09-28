import math
import numpy as np
import matplotlib.pyplot as plt
import csv
import os

here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'part1_trial1.csv')

# analysis variables
accel_array = []
force_array = []
time_array = []

# file reading
with open(filename) as file:
    csvFile = csv.reader(file)
    next(file)    
    for row in csvFile:
        if(row[0] < 8.37):
            pass
        else:
            accel_array.append(float(row[2]))
            force_array.append(float(row[4]))
            time_array.append(float(row[0]))
            




