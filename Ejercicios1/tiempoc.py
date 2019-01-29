import time
import math

def opcion1():

    f= "2*(x)*4 + 3(x)*3 - 3(x)**2 + (5*x - 1)"
    x= 0.5
    r= eval(f)

def opcion2():
    x= 0.5
    r= 2*(x)*4 + 3(x)*3 - 3(x)**2 + (5*x - 1)

def opcion3():
    x= 0.5
    r= 2*math.pow(x,4) + 3*math.pow(x,3) - 3*math.pow(x,2) + (5*x - 1)

tiempo_inicial = time.clock()
opcion1()
tiempo_final = time.clock()
exc = tiempo_final - tiempo_inicial
exc *= 1000 ;
print ("Tiempo final de ejecucion es : %.3f"  %exc )
tiempo_inicial = time.clock()
opcion2()
tiempo_final = time.clock()
exc = tiempo_final - tiempo_inicial
exc *= 1000 ;
print ("Tiempo final de ejecucion es : %.3f"  %exc)
tiempo_inicial = time.clock()
opcion3()
tiempo_final = time.clock()
exc = tiempo_final - tiempo_inicial
exc *= 1000 ;
print ("Tiempo final de ejecucion es : %.2f" %exc)
