#!/usr/bin/python
# -*- coding: utf-8 -*-
import cmath,math,os,sys;
import time

def puntofijo():
    x=0
    tolerancia=0.0001
    N=50
    gx="math.exp(-x)"
    er=100;
    i=0;
    print('iteracion\tg(f(x))\t\terror')
    starttime = time.time()
    while(i<=N and er>=tolerancia):
        temp=x
        x=eval(gx);
        er=abs((x-temp));
        print("%d\t\t%.4f\t\t%.4f"%(i,x,er));
        i+=1;

    endtime = time.time() - starttime
    print("La raiz es:",x);
    print ("El tiempo de ejecucion fue : %.4f Sg" % endtime)

puntofijo();
