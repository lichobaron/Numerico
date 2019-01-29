#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sympy import *
def taylor(f,n,y):
    #x=Symbol("x")
    x=0
    y=eval(Function(f))
    for i in range(1,n):
     if i==1:
      r=y
      #print(r)
     else:
      f=diff(f)
      e=eval(str(f))
      r=r+(e*(y)**i)/factorial(i)
    print (r)

x=Symbol("x")
f=input("Ingrese funcion: ")
n=input("Ingrese grado polinomio de Taylor: ")
n=int(n)+1
y=input("Ingrese número a calcular: ")
taylor(f,n,y)
