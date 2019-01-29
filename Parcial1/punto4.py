from sympy import *
from mpmath import *
import time

f="exp(-x)"
y=5
acum=0
x=0
i=1

while i<9:
    if i%2==0:
        d="-exp(-x)"
    else:
        d="exp(-x)"
    r= (eval(d)*y**i)/(fac(i))
    i=i+1
    acum= acum+r

print ("la aproximacion 1 es: ",acum+eval(f))
p = taylor(exp, -5, 9)
print ("la aproximacio 2 es: ", polyval(p[::-1], 2.5 - 2.0))
print ("la aproximacion es mas exacta porque presenta un reultado mas cercano al real")
