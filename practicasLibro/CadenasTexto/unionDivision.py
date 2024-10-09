# ******************************************** Metodos de union y division ********************************************
# unir
listt = "hey", "you", "que", "haces", "aqui", "pelotudo"
print ("*".join( listt))
#partir -> se parte es tres partes, la primera: previo al separador, separador mismo, el contenido que va despues del separador
che = "hey you!, how are you?"
print("particiones: ",che.partition("!"))
# partir una cadena es subcadenas
key = "python, c#, php, javascript, jquery,bootstrap"
key_sep = key.split(",")
print("Separando por comas", key_sep)
print("que tipo de dato es al separar:", type(key_sep))
