from math import *
from sympy import *
import time

fx= "x**3 +2x*2 +10*x -20" #se tiene f= "x**3 +2x*2 +10*x -20"
#sus formas son "20 / (x**2 + 2*x +10)" y "x**3 + 2*x**2 + 10*x - 20"
g1x= "20 / (x**2 + 2*x +10)"
g2x= "x**3 + 2*x**2 + 10*x - 20"
g1dx=str(diff(g1x))
g2dx=str(diff(g2x))

x=1
a= abs(eval(g1dx))
b= abs(eval(g2dx))
if a<1:
    gx=g1x
    gdx=g1dx
if b<1:
    gx=g2x
    gdx=g2dx

tolerancia=0.0001
N=50
i=1

print('iteracion\tg(f(x))\t\terror\t\tderivada')
starttime = time.time()
while i<=N:
    d= abs(float(eval(gdx)))
    if d == 0:
        print ("El metodo no aplica")
    x0=eval(gx)
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
