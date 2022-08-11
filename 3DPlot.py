import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import numpy as np

# Escolha do t'
razaoT=-0.2

# Resolução de pontos (rede n x n)
resolution = 99


def f_func(x, y):
    f = 2 * np.cos(y * np.sqrt(3)) + 4 * np.cos(x * 3 / 2) * np.cos(y * np.sqrt(3) / 2)
    return f

def z_func(x, y, positiveSide):
    res = f_func(x,y)
    z = positiveSide * np.sqrt(3 + res) - razaoT * res
    return z


coords_1d = np.linspace(-np.pi, np.pi, resolution)

[x_grid, y_grid] = np.meshgrid(coords_1d, coords_1d)

z_grid = z_func(x_grid, y_grid, 1)
z2_grid= z_func(x_grid, y_grid,-1)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel("$k_{x}$")
ax.set_ylabel("$k_{y}$")
ax.zaxis.set_rotate_label(False)
ax.set_zlabel("$E/t$", rotation=0)
ax.plot_surface(x_grid,y_grid,z_grid,rstride=1, cstride=1, cmap='viridis', vmax=4, linewidth=0, antialiased=False)
ax.plot_surface(x_grid,y_grid,z2_grid,rstride=1, cstride=1, cmap='viridis', vmax=4, linewidth=0, antialiased=False)
plt.show()