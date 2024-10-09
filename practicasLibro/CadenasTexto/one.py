# Convertir la primera letra en mayuscula

stringOne = "hola, vamos con toda!"

print(stringOne.capitalize())

# Convertir a minusculas

stringMayus = "VAMOS A PONER ESTO EN MINUSCULAS!"
stringMinus = stringMayus.lower()
print("a minusculas: ",stringMinus)

print("a mayusculas: ",stringMinus.upper())

# convertir a mayusculas o minusculas

print("convertir a minusculas:" , stringMayus.swapcase())
print("convertir a minusculas:" , stringMinus.swapcase())

#convertir una cadena a formato título

print(stringMinus.title())

tilee = "bienvenido a mi aplicacion".capitalize()

print(tilee.center(70,"*"))

# alinear a la derecha

print(tilee.rjust(60,"*"))
print(tilee.ljust(60,"*"))

#rellenar un texto anteponiendo zeros

valueX = 1550

print(str(valueX).zfill(10))

name = "fabian rene socha barbon"

# cuantas veces esta una subcadena dentro de una cadena?
print("la cantida de veces que se encuentra la letra a en la variable",name, "es: ",name.count("a"))

# buscar en una subcadena, si no encuentra la subcadena retorna -1

print(name.find("bar"))

