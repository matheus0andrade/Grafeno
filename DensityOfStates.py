from cmath import pi
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import numpy as np
import timeit

start = timeit.default_timer()

# Parametros iniciais
razaoT=-0.2

# Parametros para integração numérica
# Queremos calcular para epsilon -> 0
epsilon = 0.0382
dxDef = 0.04

# Numero de intervalos de separação entre -pi e pi
n1 = 983
n2 = 31

# f(k)
def f_func(x, y):
    f = 2 * np.cos(y * np.sqrt(3)) + 4 * np.cos(x * 3 / 2)*np.cos(y * np.sqrt(3) / 2)
    return f

# E(k)
def z_func(x, y, positiveSide):
    z = positiveSide * np.sqrt(3 + f_func(x,y)) - razaoT * f_func(x,y)
    return z

def integral(E, dx = dxDef, eps = epsilon):
    ans = 0
    for k in np.arange(- pi, pi ,dx):
        for j in np.arange(- pi, pi, dx):
                ans = ans + (1 / ((E - z_func(k, j, 1))**2 + eps**2)    +    1 / ((E - z_func(k , j, -1))**2 + eps**2))
    return (dx**2) * ans * eps * (1 / (4 * (pi**3)))



x_coords=np.linspace(-3.5, 3.5, n1)
y_coords=integral(x_coords)
x2_coords=np.linspace(-1.2, 0, n2)
y2_coords=integral(x2_coords, dx = 0.02, eps = .01)
fig, axes = plt.subplots(nrows = 1, ncols = 2, figsize = (5, 3))
axes[0].set_xlabel("$E/t$")
axes[1].set_xlabel("$E/t$")
axes[0].set_ylabel(r"$\rho(E)$")
axes[1].set_ylabel(r"$\rho(E)$")
axes[0].plot(x_coords, y_coords)
axes[1].plot(x2_coords, y2_coords)
fig.tight_layout()
stop = timeit.default_timer()

print('Time: ', stop - start)  
plt.show()