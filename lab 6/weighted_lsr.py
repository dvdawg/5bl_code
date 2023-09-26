import numpy as np
import matplotlib
import matplotlib.pyplot as plt

Normal_force = np.array([0.4704, 0.5194, 0.5684, 0.6174, 0.6664, 0.7154])
F_max = np.array([0.45, 0.52, 0.56, 0.62, 0.70, 0.764])

regression_x = np.array([0,1])
regression_y = np.array([-0.1479, -0.1479 + 1.2653])

plt.plot(Normal_force, F_max, 'o',  markersize = 1)

plt.errorbar(Normal_force, F_max, yerr = [0.008, 0.019, 0.011, 0.019, 0.010, 0.018], fmt = 'o',label = 'Error in Force')

plt.plot(regression_x,regression_y, label = 'y = -0.1479 + 1.2653x')

plt.xlabel("Normal Force (N)")
plt.ylabel("Maximum Static Friction Force (N)")
plt.title("Maximum Static Friction vs Normal Force - Sandpaper")
plt.legend()
plt.show()
