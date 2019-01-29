import numpy as np
import sympy as sp
from math import *
def f(x):
    return log(x)

def DerTresPuntoModificada(x0,h):
    c = "log(x)"
    pD = str(sp.diff(c))
    sD = str(sp.diff(pD))
    tD = str(sp.diff(sD))
    x=x0
    res = float(eval(tD))
    error = abs(res/3*h**2)
    r = 1/(2*h)*(-f(x0-h)+f(x0+h))+error
    print ( "H: %.5f"%h, " | Valor de Error : %.20f "%error,"| Resultado : %.10f"%r)

value = 1.8
DerTresPuntoModificada(value,0.1)
DerTresPuntoModificada(value,0.01)
DerTresPuntoModificada(value,0.0011)
DerTresPuntoModificada(value,0.0001)
DerTresPuntoModificada(value,0.00001)
