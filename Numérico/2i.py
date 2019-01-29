import numpy as np
import sympy as sp
from math import *
from scipy import integrate
def f(x):
    return x*exp(x)
def cuadratura(a,b):
    return (b-a)/2*(f(-(b-a)/2*1/sqrt(3)+(b+a)/2)+f((b-a)/2*1/sqrt(3)+(b+a)/2))

r = cuadratura(1,2)
print ("La aproximación de 1 a 2 es %.5f"%r)
p1 = cuadratura(1,1.5)
p2 = cuadratura(1.5,2)
r = p1 + p2
print ("La aproximación de 1 a 1.5 más 1.5 a 2 es %.5f"%r)
s = integrate.quad(f,1,2)
print ("La aproximación de scipy es ",s)
