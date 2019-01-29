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
    signo = ''
    starttime = time.time() 
    if fi * ff <0 :
        print('_____________________________________________________________________________________________________________________________________________________________________________________________')
        print('| {:^15} | {:^15} | {:^15} | {:^15} | {:^15} | {:^15} | {:^20} | {:^18} | {:^15} | {:^15} |'.format('i','xi','xf','a','xt','b','p5','p6','p7','p8'))
       
        while i <= nIte and (abs(p3) > err and abs(p4) > err and abs(ft) > err):

            xt = (xi + xf)/2
            p1 = (xi + xt)/2
            p2 = (xt + xf)/2
            ft = eval (fx,{'x' : xt})
            p3 = eval (fx,{'x' : p1})
            p4 = eval (fx,{'x' : p2})

            p5 = ff * p4
            p6 = fi * p3
            p7 = p3 * ft
            p8 = ft * p4
           
            print('| {:^15} | {:^15.4f} | {:^15.4f} | {:^15.4f} | {:^15.4f} | {:^15.4f} | {:^20.4f} | {:^18.4f} | {:^15.4f} | {:^15.4f} |'.format(i,xi,xf,p1,xt,p2,p5,p6,p7,p8))
            if p6 < 0 :
                xf = p1
            elif p7 < 0 :
                xi = p1
                xf = xt
            elif p8 < 0 :
                xi = float (xt)
                xf = p2
            elif p5 < 0 :
                xi = p2
            
            res = p1
            res2 = p2
            res3 = xt
            i+=1
    else:
        print ("\n Ingreso algun dato erroneo ")
        exit(1)
    endtime = time.time() - starttime 
    print('| {:^15} | {:^15.4f} | {:^15.4f} | {:^15.4f} | {:^15.4f} | {:^15.4f} | {:^20.4f} | {:^18.4f} | {:^15.4f} | {:^15.4f} |'.format(i,xi,xf,p1,xt,p2,p5,p6,p7,p8))
    print('_____________________________________________________________________________________________________________________________________________________________________________________________')
    print ( "El resultado aproximado es : %.4f" % ((res+res2+res3)/3 ))
    print ( "El tiempo de ejecucion fue : %.4f Sg" % endtime )
    exit(0)
main()
 
