from mpl_toolkits.mplot3d import Axes3D

import matplotlib.pyplot as plt

import numpy as np


fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')


u = np.linspace(0, 2 * np.pi, 1000)

v = np.linspace(0, np.pi, 1000)


x = np.floor(100000 * np.outer(np.cos(u), np.sin(v))
)
y = np.floor(100000 * np.outer(np.sin(u), np.sin(v))
)
z = np.floor(100000 * np.outer(np.ones(np.size(u)), np.cos(v))
)
ax.plot_surface(x, y, z)


plt.show()

