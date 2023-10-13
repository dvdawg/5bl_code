import math
import numpy as np
import matplotlib.pyplot as plt
import csv
import os

here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'one_period_part1_trial1.csv')

# found variables
slope = 15.5994

# analysis data variables
m_numerator = 0
m_denominator = 0
cu_term = 0
num_points = 0

Force_array = []
displacement_array = []
residuals_array = []

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
        residuals_array.append(Force - slope * displacement)
        
# final calculations
m = m_numerator/m_denominator
common_error = math.sqrt(cu_term / (num_points - 1))

# plotting
plt.plot(displacement_array, residuals_array, "o", markersize = 1)

plt.xlabel("Displacement (m)")
plt.ylabel("Residuals")
plt.title("Residual graph - Spring on a Horizontal Surface")
plt.legend()
plt.show()

