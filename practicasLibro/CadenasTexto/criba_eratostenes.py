def eratostenes (n):
    print (n)
    criba = (n+1) * [True]
    i = 2
    while i**2 <=n:
        #print('i**2:',i**2)
        print('criba **2',criba[i**2])
        if (criba[i]):
            j = 2
            while i*j <=n:
                print('i',i, 'j',j,  'i*j:', i*j )
                criba[i*j] = False
                j+=1
        i+=1
    primos = []
    k = 2
    while k <=n:
        if(criba[k]):
            primos.append(k)
        k+=1
    return primos


print(eratostenes(120))
