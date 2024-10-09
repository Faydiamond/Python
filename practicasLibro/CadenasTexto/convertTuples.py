# ******************************************** Conversion de tupla a lista ****************************************************************************
materias = ("Fisica","Quimica","Ingles","Filosofia")
print(type(materias))
print(materias)
materiasList = list(materias)
print(type(materiasList))
print(materiasList)
# unir tuplas
one  = (1,2,3,4)
twoo = (5,6,7,8,9,10)
res  = one + twoo
print(res)
max = max(res)
min = min(res)
print("el valor maximo de la tupla es {maxx} y el valor minimo es {minimo}".format(maxx=max,minimo=min))
# cuantos elementos tiene una lista
howList = len(res)
print("la tupla tiene {} elementos".format(howList))
