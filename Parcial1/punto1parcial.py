from math import *
from sympy import *
import time
import sys

a=1
b=0
c=3
gx=str(a)+"*x**2+"+str(b)+"*x+"+str(c)
g1dx=str(diff(gx))
g2dx=str(diff(g1dx))

x=1.5
i=1
N=50
tolerancia=0.001
r=(b**2-4*a*c)

if r<0:
    q= -b/(2*a)
    i= (abs(r))**(1/2)/(2*a)
    print ("La raiz es ",q,"+",i,"i")
    sys.exit(0)


print('iteracion\tg(f(x))\t\terror\t\tderivada_1\t\tderivada_2')
starttime = time.time()
while i<=N:
    a=float(eval(gx))
    b=float(eval(g1dx))
    c=float(eval(g2dx))
    d=(abs(b)**2 - a*c)
    x0=x- a*b/d
    er=abs(x0-x)
    print("%d\t\t%.5f\t\t%.5f\t\t%.5f\t\t%.5f"%(i,x0,er,b,c))
    if er<tolerancia:
        endtime = time.time() - starttime
        print("La raiz es ",x0)
        print ("El tiempo de ejecucion fue : %.4f Sg" % endtime)
        break
    i=i+1
    x=x0
if i>=N:
    print("El metodo no converge ")
