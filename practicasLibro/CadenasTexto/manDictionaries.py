# ******************************************** Manipulación de diccionarios ***********************************************************************
dictionaryy = {"fabian" : 27, "Juana": 28 , "Andrea" : 32 , "Sofia": 35}
print(dictionaryy)
# limpiar un diccionario
#dictionaryy.clear()
#copiar un diccionario
copyy = dictionaryy.copy()
print(copyy)
# crear un nuevo diccionario desde las claves de una secuencia
secuence = ["color",'Olor',"Sabor"]
dictt = dict.fromkeys(secuence,["defecto"])
print (dictt)
# concatenar diccionarios
dictOne = {"marca": "Lacoste", "Talla": "39 - 40"}
dicTwoo = {"precio": 250.000, "color": "Blanco con cafe","material":"Cuero"}
dictOne.update(dicTwoo)
print(dictOne)
#conocer el valor de una clave
print("la clave de {} es : {}".format("color",dictOne.get("color") ))
#saber si una clave existe en un diccionario
print( "Talla" in dictOne)
#obtener las claves y valores de un diccionario
for key,valu in dictOne.items():
    print(key,valu)

# obtener las claves de un diccionario
for claves in dictOne.keys():
    print(claves)

# Obtener valores de un diccionario
for values in dictOne.values():
    print(values)

#obtener valores en una lista
valores = list(dictOne.values())
llavess = list(dictOne.keys())
print(llavess, valores)
#cantidad de elementos en un diccionario
print(len(dictOne))
