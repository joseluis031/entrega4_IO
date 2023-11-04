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

z1 = "10 - 2*x"
z2 = "20 - 2*x"
z3 = "30 - 2*x"
plot(f1, f2, z1, z2, z3, (x, 0, 10), title='1 cuadrante', xlabel='x1', ylabel='x2', legend=True)

# 2 cuadrante
f1 = 8 + x
f2 = 18 + 3*x

z1 = "10 + 2*x"
z2 = "20 + 2*x"
z3 = "30 + 2*x"
plot(f1, f2, z1, z2, z3, (x, -10, 0), title='2 cuadrante', xlabel='x1', ylabel='x2', legend=True)

# 3 cuadrante
f1 = -8 - x
f2 = -18 - 3*x

z1 = "-10 - 2*x"
z2 = "-20 - 2*x"
z3 = "-30 - 2*x"
plot(f1, f2, z1, z2, z3, (x, -10, 0), title='3 cuadrante', xlabel='x1', ylabel='x2', legend=True)

# 4 cuadrante
f1 = -8 + x
f2 = -18 + 3*x

z1 = "-10 + 2*x"
z2 = "-20 + 2*x"
z3 = "-30 + 2*x"
plot(f1, f2, z1, z2, z3, (x, 0, 10), title='4 cuadrante', xlabel='x1', ylabel='x2', legend=True)

