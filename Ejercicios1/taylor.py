#/usr/bin/env python3
# -*- coding: utf-8 -*-

from sympy import *
from sympy.plotting import *
import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np

rcParams['text.latex.unicode'] = True
rcParams['text.usetex'] = True
rcParams['text.latex.preamble'] = '\\usepackage{amsthm}', '\\usepackage{amsmath}', '\\usepackage{amssymb}',
'\\usepackage{amsfonts}', '\\usepackage[T1]{fontenc}', '\\usepackage[utf8]{inputenc}'

x = symbols('x')
init_printing(use_unicode=True)
pprint('Introduce la función para calcular su polinomio de Taylor: ')
expr = eval(input())
pprint('La función es: ')
pprint(expr)
pprint(r'Introduce el punto local x_0: ')
x0 = float(input())
pprint('Introduce el grado del polinomio: ')
n = int(input())
taylor = expr.series(x, x0, n).removeO()
pprint('El Polinomio de Taylor  de orden {0} centrado en {1} es:\n '.format(n, x0))
pprint(taylor)
f = lambdify(x, expr, 'numpy')
g = lambdify(x, taylor, 'numpy')

fig, ax = plt.subplots()
title = r'$Polinomio \; De \; Taylor \; (x_0={0},\; n={1})$'.format(x0, n)
ax.set_title(title)
t = np.linspace(-6.0, 6.0, 1000)
ax.axis([-6, 6, -1, 6])

ax.set_xlabel('x', color='blue')
ax.set_ylabel('y', color='blue')

ax.grid('on')

ax.plot(t, f(t), 'b-', lw=1.5)
ax.plot(t, g(t), 'r-', lw=1.5)

# Drawing Our Legend
text1 = r'$f(x)={}$'.format(latex(expr))
text2 = r'$g(x)={}$'.format(latex(taylor))

plt.legend([text1, text2])

plt.show()
