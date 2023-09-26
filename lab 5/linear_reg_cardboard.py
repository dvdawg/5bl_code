import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import math

Normal_force = np.array([1.9404, 2.3324, 2.7244, 3.1164, 3.5084, 3.2144])
F_max = np.array([0.49, 0.67, 0.76, 0.848, 0.932, 0.784])

regression_x = np.array([0,4])
regression_y = np.array([0.04567, 0.04567 + 0.2501 * 4])

plt.plot(Normal_force, F_max, 'o',  markersize = 5)

plt.errorbar(Normal_force, F_max, yerr = [0.008, 0.019, 0.011, 0.019, 0.01, 0.018], fmt = 'o',label = 'Error in Force')

plt.plot(regression_x,regression_y, label = 'y = 0.04567 + 0.2501x')

plt.xlabel("Normal Force (N)")
plt.ylabel("Maximum Static Friction Force (N)")
plt.title("Maximum Static Friction vs Normal Force - Cardboard")
plt.legend()
plt.show()

common_error = math.sqrt((1/4) * (0.04567 - 0.2501 * Normal_force[0]))
print(common_error)