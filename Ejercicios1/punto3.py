from sympy import limit, Symbol, oo, sqrt, Rational, log, exp, cos, sin, tan, pi, asin, together, root, Function, diff
import math

def differentiable(f,a):
    g= str(diff(f))
    x=a
    r=float(eval(g))
    y= (Function(f)- eval(f))
    z= str(y)+"/(x+"+str(a)+")"
    s= eval(z)
    if r == s
        return True
    else:
        return False


def rolle(f,a,b):
    x=1

f = "(x-2)*sin(x)*log(x+2)"
differentiable(f,-1)
