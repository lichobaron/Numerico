import time
import math

def opcion1():
    tiempo_inicial = time.clock()
    f= "2*(x)**4 + 3*(x)**3 - 3*(x)**2 + (5*x - 1)"
    x= 0.5
    r= eval(f)
    tiempo_final = time.clock()
    tiempo_ejecucion = tiempo_final - tiempo_inicial
    tiempo_ejecucion*=1000
    print 'El tiempo de ejecucion para la opcion 1 fue de:',tiempo_ejecucion

def opcion2():
    tiempo_inicial = time.clock()
    x= 0.5
    r= 2*(x)**4 + 3*(x)**3 - 3*(x)**2 + (5*x - 1)
    tiempo_final = time.clock()
    tiempo_ejecucion = tiempo_final - tiempo_inicial
    tiempo_ejecucion*=1000
    print 'El tiempo de ejecucion para la opcion 2 fue de:',tiempo_ejecucion

def opcion3():
    tiempo_inicial = time.clock()
    x= 0.5
    r= 2*math.pow(x,4) + 3*math.pow(x,3) - 3*math.pow(x,2) + (5*x - 1)
    tiempo_final = time.clock()
    tiempo_ejecucion = tiempo_final - tiempo_inicial
    tiempo_ejecucion*=1000
    print 'El tiempo de ejecucion para la opcion 3 fue de:',tiempo_ejecucion

def main():
    opcion1()
    opcion2()
    opcion3()


if __name__ == '__main__':
    main()
