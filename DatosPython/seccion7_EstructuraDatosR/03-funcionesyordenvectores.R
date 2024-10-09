#sapply nos ahorra recorrer vectores
# sacar la raiz a cada uno de los elementos de un vector

vec <- 1:30
#print(vec)
#espero el vecto y que va hacer como argumentos.
raiz <- sapply(vec,FUN = function(elemento){sqrt(elemento)})
#print(raiz)
#medidas estadisticas
#print(length(vec))
#print(mean(vec))
#print(cumsum(vec))

cuadrado <- sapply(vec, function(x){x^2})
#print(cuadrado)

cuadrado1 = function(y){y^2}

#print(sapply(vec, FUN = cuadrado1))

#ordenar vector sort
numbers <- c(100,50,10,8,2,0,1,20,70,80,90,4)
orden <- sort(numbers,decreasing=F)
#print(orden)

#Ejercicio
#1:

letras <- c('x','z','j','e','k','a','b','m','c','d')
decree <- function(k){sort(k)}
print(sapply(numbers, FUN = decree))

print(sort(numbers,decreasing=T))