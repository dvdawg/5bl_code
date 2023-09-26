#Three lines to make our compiler able to draw:
import sys
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0.49,0.59,0.69,0.78,0.88,0.98])
ypoints = np.array([0.022,0.03,0.038,0.046,0.054,0.062])
x2= np.array([0,1])
y2 = np.array([0,0.058])
x3 = np.array([0.45,0.55])
y3 = np.array([0.45 * 0.058, 0.55 * 0.058])

plt.plot(xpoints, ypoints,'o')
plt.plot(x2,y2, label = 'y = 0.058x')
plt.errorbar(xpoints,ypoints,yerr = [0.008, 0.019, 0.011, 0.019, 0.010, 0.018],fmt = 'o',label = 'Error in Length')
plt.plot(x3, y3,label = 'm=0.058, error in m = 0.0045')
plt.title('Force vs.Change in Euillibirum Length')
plt.xlabel('Force,F(N)')
plt.ylabel('Change in Equillibrium Length,L(m)')
plt.legend()
plt.show()

#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
