import matplotlib.pyplot as plt
from scipy.interpolate import InterpolatedUnivariateSpline
import scipy.interpolate as si
import numpy as np

def mostrarImagen():
    im = plt.imread("mano1.png")
    implot = plt.imshow(im, origin='upper', extent=[0,10,0,10])
    plt.grid(True)
    plt.show()


def main():
    print("Digitar: Numero de puntos seguido de coor y , coor x por el numero de puntos")
    mostrarImagen()
    n=int(input())
    x0, y0 = [], []
    i=0
    while i<n:
        x0.append(float(input()))
        y0.append(float(input()))
        i=i+1

    ref= float(x0[0])
    print(x0)
    i=0
    while i<n:
        if x0[i] < ref:
            x0[i]= ref+0.2
        ref=x0[i]
        i=i+1
    print(x0)

    result=zip(x0,y0)
    P=list(result)
    xi, yi = zip(*P)  # 21 puntos de interpolación
    x = np.linspace(min(xi), max(xi), num=100)  # Dominio
    #spline
    y1d = np.interp(x, xi, yi)
    ysp = InterpolatedUnivariateSpline(xi, yi)
    i=0
    while i<n:
        if yi[i] < 5:
            if x[i] < 5:
                x[i]=x[i]+2
            if x[i] > 5:
                x[i]=x[i]-2

        i=i+1
    plt.plot(x,yi)
    plt.grid(True)
    #plt.xlim(0, 10)
    #plt.ylim(0, 10)
    plt.show()

if __name__ == '__main__':
    main()
