from math import *
from sympy import *
import time

gx="8**x -25" #funcion inversa transformada
g1x=str(diff(gx))
x=1
tolerancia=0.0001
N=50
i=1
print('iteracion\tg(f(x))\t\terror\t\tderivada')
starttime = time.time()
while i<=N:
    d= float(eval(g1x))
    if d == 0:
        print ("El metodo no aplica")
    x0=x-float(eval(gx))/d
    er=abs(x0-x)
    print("%d\t\t%.5f\t\t%.5f\t\t%.5f"%(i,x0,er,d));
    if er<tolerancia:
        endtime = time.time() - starttime
        print("La raiz es ",x0)
        print ("El tiempo de ejecucion fue : %.4f Sg" % endtime)
        break
    i=i+1
    x=x0
if i>=N:
    print("El metodo no converge ")
