from sympy import *
#Funcion que recibe una coordenada en X y Y y retorna el respectivo valor
def f(x,y):
    ax = [0,100,200,300,400]
    ay = [0,50,100,150,200]
    table= [[0,0,4,6,0],
            [0,3,5,7,3],
            [1,5,6,9,5],
            [0,2,3,5,1],
            [0,0,1,2,0]]
    yi= ax.index(x) #Obtener la posicion de y en la matriz
    xi= ay.index(y) #Obtener la posicion de x en la matriz
    return table[xi][yi] #Retornas el valor segun los indices x,y

#Metodo de simpson para una variable
def simpson(f,a,b,m):
    h = (b - a)/float(m) #Calculo del paso h
    sum1 = 0
    for i in range(1, int(m/2 + 1)):
        sum1 += f(a + (2*i - 1)*h)  #Calculo de la funcion en x1
    sum1 *= 4
    sum2 = 0
    for i in range(1, int(m/2)):
        sum2 += f(a + 2*i*h)  #Calculo de la funcion en x2
    sum2 *= 2
    approx = (b - a)/(3.0*m)*(f(a) + f(b) + sum1 + sum2) #Calculo de la aproximacion segun metodo de simpson
    return approx

def simpson2(f,ax,bx,ay,by,mx,my):
    x= Symbol('x')
    dy= (by - ay)/my #Calculo del paso en y
    v= ay #Establecer un y fijo
    r= []
    for i in range (0,my+1):
        def g(x): return f(x,v)
        u= simpson(g,ax,bx,mx) #Aproximacion de Simpson en x con un y fijo
        r= r+[u]
        v=v+dy #Mover paso en y
    s=0
    for i in range(1,my):
        s=s+2*(2-(i+1)%2)*r[i] #Suma de los volumenes obtenidos
    s= dy/3*(r[0]+s+r[my]) #Calculo de la aproximacion segun metodo de simpson
    return s

print("El area del lago es: ",simpson2(f,0,400,0,200,4,4)," metros cubicos.")
