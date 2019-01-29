from sympy import *
from mpmath import *
import math
import time

fx1= "math.log(x + 2,10)" #se tiene f= "x**3 +2x*2 +10*x -20"
fx2= "-sin(x)"
#sus formas son "20 / (x**2 + 2*x +10)" y "x**3 + 2*x**2 + 10*x - 20"
fd1="1/(x+2)"#str(diff(fx1)) #se toma debido a que es la corta el eje en la interpretacion grafica
fd2="-cos(x)"#str(diff(fx2))
x=1
x1=x
x2=x
tolerancia=0.1
N=50
i=1
print('iteracion1\tg(f(x))1\t\terror1\t\tderivada1\t\t\titeracion2\tg(f(x)2)\t\terror2\t\tderivada2')
starttime = time.time()
while i<=N:
    aux=x
    x=x1
    d1=float(eval(fd1))
    a1=float(eval(fx1))
    x01=x1-a1/d1
    x=aux
    er1=abs(x01-x1)
    aux=x
    x=x2
    x=aux
    d2= float(eval(fd2))
    a2= float(eval(fx2))
    x02=x2-a2/d2
    x=aux
    er2=abs(x02-x2)
    print("%d\t\t%.6f\t\t%.6f\t\t%.6f\t\t\t%d\t\t%.6f\t\t%.6f\t\t%.6f"%(i,x01,er1,d1,i,x02,er2,d2));
    if abs(1-x01)<= abs(1-x02):
        endtime = time.time() - starttime
        print("Se cruzan en %.6f" %x01)
        print ("El tiempo de ejecucion fue : %.4f Sg" % endtime)
        break
    i=i+1
    x1=x01
    x2=x02
if i>=N:
    print("El metodo no converge ")
