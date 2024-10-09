#crear vector
vec <- seq(1,58,by=4)
print(vec)

#Elegir un elemento
print(vec[5])

#eliminar elementos de un vector
print(vec[-c(5,6)])

#condicion muestres los diferentes a 40 pero mayores a 49
print(vec[vec != 40 & vec>=49])

#conocer la penultima posicion
print(vec[length(vec)-1])
