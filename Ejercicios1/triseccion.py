from math import *
import time

def main():
    fx = input('Ecuacion f(x) = ')
    xi = float(input('Limite inferior : '))
    xf = float(input('Limite superior : '))
    err = float(input('Ingresa la tolerancia : '))
    nIte = ceil((log(xf - xi) - log(err)) / log(2))
    i = 1

    fi = eval(fx,{'x' : xi})
    ff = eval(fx,{'x' : xf})
    ft = 1E10
    p3 = 1E10
    p4 = 1E10
    res = 0 
    res2 = 0
    prom = 1E10
    signo = ''
    starttime = time.time() 
    if fi * ff <0 :
        print('_________________________________________________________________________________________________________________________________________________')
        print('| {:^15} | {:^15} | {:^15} | {:^15} | {:^15} | {:^15} | {:^15} | {:^15} |'.format('i','a','b','ft1','ft2','cambio','xi','xf'))
        #print('________________________________________________________________________________________________________________________________')
        while i <= nIte and (abs(p3) > err and abs(p4) > err   ):

            xt = (xi + xf)/2
            p1 = (xi + xt)/2
            p2 = (xt + xf)/2
            p3 = eval (fx,{'x' : p1})
            p4 = eval (fx,{'x' : p2})
            p5 = ff * p4
            p6 = fi * p3
            p7 = p3 * p4

            print('| {:^15} | {:^15.4f} | {:^15.4f} | {:^15.4f} | {:^15.4f} | {:^15} | {:^15.4f} | {:^15.4f} |'.format(i,p1,p2,p3,p4,signo,xi,xf))          
            
            if p6 < 0 :
                xf = p1
                signo = 'INFERIOR'
            if p7 < 0 :
                xi = p1
                xf = p2
                signo = 'MITAD'
            if p5 < 0 :
                xi = p2
                signo = 'SUPERIOR'
           
            res = p1
            res2 = p2
            prom = abs(p3) + abs(p4) / 2 
            i+=1
    else:
        print ("\n Ingreso algun dato erroneo ")
        exit(1)
    endtime = time.time() - starttime ; 
    print('| {:^15} | {:^15.4f} | {:^15.4f} | {:^15.4f} | {:^15.4f} | {:^15} | {:^15.4f} | {:^15.4f} |'.format(i,p1,p2,p3,p4,signo,xi,xf))
    print('_________________________________________________________________________________________________________________________________________________')
    
    
    print ( "El resultado aproximado es : %.4f" % ((res+res2)/2 ))
    print ( "El tiempo de ejecucion fue : %.4f Sg" % endtime )
    exit(0)
main()
 
