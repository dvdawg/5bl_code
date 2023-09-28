import math
import numpy as np
import matplotlib.pyplot as plt
import csv
import os

here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'part1_trial1.csv')

# found variables
slope = 15.63988

# analysis data variables
m_numerator = 0
m_denominator = 0
cu_term = 0
num_points = 0

Force_array = []
displacement_array = []

#file reading
with open(filename) as file:
    csvFile = csv.reader(file)
    next(file)    
    for row in csvFile:
        Force = float(row[1]) * (-1)
        displacement = float(row[2])
        num_points += 1
        Force_array.append(Force)
        displacement_array.append(displacement)

        m_numerator += Force * displacement
        m_denominator += displacement**2

        cu_term += (Force - slope*displacement)**2
        
# final calculations
m = m_numerator/m_denominator
common_error = math.sqrt(cu_term / (num_points - 1))

# plotting

regression_x = [0, 0.282]
regression_y = [0, 15.63988 * 0.282]
plt.plot(regression_x,regression_y, label = 'y = ' + str(slope) + 'x')
plt.xlabel("Displacement (m)")
plt.ylabel("-1 * Force (N)")
plt.title("Force vs Displacement")
plt.legend()
plt.show()

