import math #Libreria para el uso de la función exponencial
f= "(9.8*68.1)/c * (1-math.exp((-c/68.1*10)))-40" #Función a evaluar
xi= 0.01 #Límete Inferior
xf= 20 #Límite Superior
error= 0.0001
raiz=(xi+xf)/2 #Valor medio entre los límites
c=raiz
while abs(eval(f))>error:    #Ciclo
 raiz=(xi+xf)/2
 c=xi           #Reemplazar c por el límite inferior
 r1=eval(f)     #Se evalúa en la función
 c=raiz         # Reemplazar c por el valor medio
 r2=eval(f)     #Se evalúa en la función
 if r1*r2<0 :   #Se evalúa la expresión para evaluar la función en el próximo
   xf=raiz      #ciclo por la izquierda del intervalo
 elif r1*r2>0:  #Se evalúa la expresión para evaluar la función en el próximo
   xi=raiz      #ciclo por la derecha del intervalo
 c=raiz
print("C= ",raiz) #Resultado aproximado de la variable c
