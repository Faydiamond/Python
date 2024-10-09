# ******************************************** Metodos de validación ****************************************************************************
name = "fabian rene socha barbon"
# saber si una cadena comienza con una subcadena determinada
print(name.startswith("barbon",18))
print(name.endswith("barbon",18))
# saber si una cadena es alfanumerica
thingg = "pepe ".capitalize()
print("es alfanumerica: " ,thingg.isalnum())
# saber si una cadena es alfabetica
print("es alfabetica: ", name.isalpha())
# saber si una cadena es numerica
numbers = "1221"
print("Es numerica: ",numbers.isdigit())
# saber si contiene solo minusculas
print("Contiene solo minuisculas? ",name.islower())
print("Contiene solo mayusculas? ",name.isupper())
# contiene solo espacios en blanco
print("Solo espacios en blanco: ",name.isspace())
# esta formateada como título?
print("tiene formato titulo: ",name.istitle())
