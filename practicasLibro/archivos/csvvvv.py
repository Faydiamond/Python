# ******************************************** Manipulación de archivos Csv***********************************************************************
from csv import reader

with open("data.csv","r") as filee:
    document = reader(filee, delimiter=';', quotechar='"')
    cabeceras = next(document)
    for fila in document:
        print((" ".join(fila)))
#escribir en un archivo con cabecera
#crear la cabecera como una lista
cabeceraa = ["id_us","nombre","nombre1","correo","usuario","edad","fk_ciudad"]
# crear una mattriz con las listas de sus coincidencias
matrizz = [
    dict(id_us=60,nombre="Pablo",nombre1="Daniel",correo="pablo@gmailcom.co",usuario="osvaldoo",edad=36,fk_ciudad=1),
    dict(id_us=61,nombre="Pablo",nombre1="Julian",correo="pabloJu@gmailcom.co",usuario="PaloDan",edad=36,fk_ciudad=1),
    dict(id_us=62,nombre="Pablo",nombre1="Andres",correo="pabloAn@gmailcom.co",usuario="PaloAnn",edad=34,fk_ciudad=1),
]

print (matrizz)
#escribir
from csv import DictWriter

with open ("data.csv", "w") as dataW:
    documentt = DictWriter(dataW, delimiter=';', quotechar='"', fieldnames=cabeceraa)
    documentt.writeheader()
    documentt.writerows(matrizz)

from csv import reader
with open("data.csv","r") as reData:
    do = reader(reData,delimiter=';', quotechar='"')
    print(do)


