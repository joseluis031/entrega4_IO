'''Dado el siguiente problema de programación lineal
Max Z = 2x1 + x2
Con las restricciones:
x1 + x2 <= 8
3x1 + x2 <= 18
x1; x2 >= 0
Representar gráficamente y mediante un modelo de programación lineal los problemas 
simétricos equivalentes en cada uno de los cuatro cuadrantes.
1 cuadrante
x1 >= 0
x2 >= 0
2 cuadrante
x1 <= 0
x2 >= 0
3 cuadrante
x1 <= 0
x2 <= 0
4 cuadrante
x1 >= 0
x2 <= 0
'''

import numpy as np
from sympy import symbols
from sympy.plotting import plot

x = symbols('x')

# 1 cuadrante
f1 = 8 - x
f2 = 18 - 3*x

z1 = "8 - 2*x"
z2 = "18 - 2*x"

plot(f1, f2, z1, z2, (x, 0, 10), title='1 cuadrante', xlabel='x1', ylabel='x2', legend=True)

# 2 cuadrante
f1 = 8 + x
f2 = 18 + 3*x

z1 = "8 + 2*x"
z2 = "18 + 2*x"

plot(f1, f2, z1, z2, (x, -10, 0), title='2 cuadrante', xlabel='x1', ylabel='x2', legend=True)

# 3 cuadrante
f1 = -8 - x
f2 = -18 - 3*x

z1 = "-8 - 2*x"
z2 = "-18 - 2*x"

plot(f1, f2, z1, z2, (x, -10, 0), title='3 cuadrante', xlabel='x1', ylabel='x2', legend=True)

# 4 cuadrante
f1 = -8 + x
f2 = -18 + 3*x

z1 = "-8 + 2*x"
z2 = "-18 + 2*x"

plot(f1, f2, z1, z2, (x, 0, 10), title='4 cuadrante', xlabel='x1', ylabel='x2', legend=True)

# los 4 cuadrantes en una sola gráfica

import matplotlib.pyplot as plt
import numpy as np

# Define las funciones
def f1(x):
    return 8 - x

def f2(x):
    return 18 - 3 * x

def f3(x):
    return 8 + x

def f4(x):
    return 18 + 3 * x

def f5(x):
    return -8 - x

def f6(x):
    return -18 - 3 * x

def f7(x):
    return -8 + x

def f8(x):
    return -18 + 3 * x

# Valores de x para la gráfica
x = np.linspace(-10, 10, 400)

# Gráfica de las funciones
plt.plot(x, f1(x), label='8 - x')
plt.plot(x, f2(x), label='18 - 3x')
plt.plot(x, f3(x), label='8 + x')
plt.plot(x, f4(x), label='18 + 3x')
plt.plot(x, f5(x), label='-8 - x')
plt.plot(x, f6(x), label='-18 - 3x')
plt.plot(x, f7(x), label='-8 + x')
plt.plot(x, f8(x), label='-18 + 3x')

# Configuración de la gráfica
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.title('Gráfico en los 4 cuadrantes')
plt.xlabel('x1')
plt.ylabel('x2')
plt.legend(loc='best')

# Muestra la gráfica
plt.grid()
plt.show()

