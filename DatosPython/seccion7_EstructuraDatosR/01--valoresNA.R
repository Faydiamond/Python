#los objetos nuulos no apareven en el print
#NA <- no disponible

vec <- 1:15
vec[16] <- 2.5 
vec[length(vec)+5] = 3
#print(vec)

#si intento sumar , el resultado es NA
su <- sum(vec)
#print(su)
#Eliminar NA
print(sum(vec,na.rm = T))
#como saber si tengo valores NA, tenga en cuenta que los NA no se puden comparar
#print(is.na(vec))
#que posiciones estan los NA
#print(which(is.na(vec)))
#los Na por lo general se cambian por la media
copy.vec = vec
copy.vec[is.na(copy.vec)] = mean(copy.vec,na.rm=T)
print(copy.vec)
#omitir na <- no recomendar
omitir <- na.omit(vec)


attr(omitir,"na.action") = NULL
print(omitir)