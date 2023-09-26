import numpy as np
import matplotlib
import matplotlib.pyplot as plt

t_squared = np.array([1.81118, 2.68567, 4.52924, 6.26301, 8.1282, 9.34586])
moment_inertia = np.array([63.0436, 88.3246, 138.8870, 189.4490, 240.0110, 290.5730])

regression_x = np.array([0,1])
regression_y = np.array([-0.1479, -0.1479 + 1.2653])

plt.plot(t_squared, moment_inertia, 'o',  markersize = 1)

plt.errorbar(t_squared, moment_inertia, yerr = [0.008, 0.019, 0.011, 0.019, 0.010, 0.018], fmt = 'o',label = 'Error in Force')

plt.plot(regression_x,regression_y, label = 'y = -0.1479 + 1.2653x')

plt.xlabel("Normal Force (N)")
plt.ylabel("Maximum Static Friction Force (N)")
plt.title("Maximum Static Friction vs Normal Force - Sandpaper")
plt.legend()
plt.show()
