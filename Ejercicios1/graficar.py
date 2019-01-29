#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
from matplotlib import pyplot
# Función cuadrática.
def f1(x):
    return (x-2)**2 - math.log10(x)
# Función lineal.
#def f2(x):
#    return 4*x + 1
# Valores del eje X que toma el gráfico.
x = range(1, 20)
# Graficar ambas funciones.
pyplot.plot(x, [f1(i) for i in x])
#pyplot.plot(x, [f2(i) for i in x])
# Establecer el color de los ejes.
pyplot.axhline(0, color="black")
pyplot.axvline(0, color="black")
# Limitar los valores de los ejes.
pyplot.xlim(-1, 3)
pyplot.ylim(-1, 3)
# Guardar gráfico como imágen PNG.
pyplot.savefig("output.png")
# Mostrarlo.
pyplot.show()
