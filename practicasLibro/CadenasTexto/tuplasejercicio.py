
numbers_str = input('Escribe una secuencia de números separados por un espacio: ').split(' ')
numbers_str.sort()
print(numbers_str)
#print(type(numbers_str))
number = [int(x) for x in numbers_str]
#print(number)
#print(sum(number))

#print(len(number))
i = 0
sumaa = 0
while i < len(number):
    #print(number[i])
    sumaa += number[i]
    print(sumaa)
    i+=1