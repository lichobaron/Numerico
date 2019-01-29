from math import *
from sympy import *
import time


gx="2**x -1.3"
x=-1
tolerancia=0.0001
N=1000
i=1
x0=0
print('iteracion\tg(f(x))\t\terror')
starttime = time.time()
while i<=N:
    fx=eval(gx)
    aux=x
    x=x0
    fx0=eval(gx)
    x=aux
    xi=x-fx*(x-x0)/(fx-fx0)
    er=abs(x0-x)
    print("%d\t\t%.4f\t\t%.4f"%(i,x0,er));
    if er<tolerancia:
        endtime = time.time() - starttime
        print("La raiz es %.4f" %x0)
        print ("El tiempo de ejecucion fue : %.4f Sg" % endtime)
        break
    i=i+1
    x0=x
    x=xi
