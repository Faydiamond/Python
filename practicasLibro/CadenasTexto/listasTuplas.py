# ******************************************** Metodos de listas y tuplas ****************************************************************************
# agregar elementos a la lista en la ulti8ma posicion
myList = ["Daniel","Julian","Pedro","Carlos","Juana"]
myList.append("Arturo")
print(myList)
#agregar varios elementos al final de la lista extend
myList.extend(["Daniela","Julieta","Yesica","Milena"])
print(myList)
# agreghar elemento en una posicion determinada
myList.insert(2,"Ana")
print(myList)
# eliminar el elemento de la ultima posicion
myList.pop()
print(myList)
#eliminar elemento por su indice
myList.pop(2)
print(myList)
# eliminar elementos por su valor
myList.remove("Arturo")
print(myList)
# invertir orden en una lita
print("reverse", myList.reverse())