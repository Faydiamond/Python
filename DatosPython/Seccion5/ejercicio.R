#Preguntas de esta tarea
#Si hubiéramos empezado a contar segundos a partir de las 12 campanadas que marcan el inicio de 2018,
#¿a qué hora de qué día de qué año llegaríamos a los 250 millones de segundos? ¡Cuidado con los años
#bisiestos!
#Solucion:
#pasar a minutos
  
minutes <- 250000000 /60
print (minutes)

hours     <-  minutes%/%60
minutes.r <- minutes %% 60
print(hours)
print(minutes.r)

days <- hours%/%24
print(days)

days.hours <- hours%%24
print(days.hours) #cantidad de horas

year <- days%/%365
print(year)

year.day <- (days%%365)-2
print(year.day)

#respesta = 2018+7años+336dias+12horas
#año:2025
#dia: 2 diciembre
#hora: 12:26.66

#2-Cread una función que os resuelva una ecuación de primer grado (de la forma Ax+B=0).
#Es decir, vosotros tendréis que introducir como parámetros los coeficientes (en orden) 
#y la función os tiene que devolver la solución. Por ejemplo, si la ecuación es 2x+4=0, 
#vuestra función os tendría que devolver -2.

ecu.primer.grado <- function(a,b)
{
  print(-b/a)
}
ecu.primer.grado (5,3)
ecu.primer.grado (7,4)
ecu.primer.grado (1,1)

#3- Dad una expresión para calcular 3e-?? y a continuación, dad el resultado que habéis obtenido
#con R redondeado a 3 cifras decimales.

calculate <- round(Mod(2+3i^2/(5+8i)),3)
print(calculate)
  
print(round(Mod((2+3i)^2/(5+8i)),3))
  