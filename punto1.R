##analisis numerico
#instalar paqute Matrix


#install.packages("Matrix")#instalar paquete
library(Matrix)
#install.packages("PolynomF")#instalar paquete
library(PolynomF)
#install.packages("pracma")
library(pracma)
#install.packages("barylag")
library(barylag)


#interpolacion de lagrange
lagrange = function(x,y,a){
n = length(x)
if(a < min(x) || max(x) < a) stop("No está interpolando")
X = matrix(rep(x, times=n), n, n, byrow=T)
mN = a - X; diag(mN) = 1
mD = X - t(X); diag(mD) = 1
Lnk = apply(mN, 1, prod)/apply(mD, 2, prod)
sum(y*Lnk)
}
##prueba
x = c(6,8,10,12,14,16,18,20)
y =  c(7,9,12,18,21,19,15,10)


for(i in 1:n){
	p=(x[i+1]+x[i])/2
	print(p)
	if(max(x) < p){
		lagrange(x[1:n],y[1:n], p)
	}
	
}

plot(x,y, pch=19, cex=1, col = "red", asp=1,xlab="Hora", ylab="Temperatura", main="Diagrama Temperatura vs Tiempo ")
##graficar el polinomio