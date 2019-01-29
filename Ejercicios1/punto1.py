from sympy import limit, Symbol, oo, sqrt, Rational, log, exp, cos, sin, tan, pi, asin, together, root
import math

def evalLimit(a):
    x = Symbol("x")
    return float(limit((x-2)**2 - log(x), x, a))

def continouos(a):
    x = Symbol("x")
    r= evalLimit(a)
    x=a
    s=float((x-2)**2 - log(x))
    if r == s:
        return True
    else:
        return False

def intermediateValue(a,b):
    if continouos(a) and continouos(b):
        x = Symbol("x")
        x=a
        r=float((x-2)**2 - log(x))
        x=b
        s=float((x-2)**2 - log(x))
        if(r != s and (r<s or s<r)):
            return True
        else:
            return False
    else:
        return False

if intermediateValue(1,2):
    print "existe un x entre 1 y 2 para el cual la funcion es igual a 0"

if intermediateValue(math.e,4):
    print "existe un x entre e y 4 para el cual la funcion es igual a 0"
