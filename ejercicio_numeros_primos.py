rango=int(input("Ingresa el rango hasta donde quieres encontrar números primos: "))
primos=[1]
if(rango==1):
    print(primos)
else:
    for comienzo in range(2, rango+1):
        contador=0
        for divisor in range(1, comienzo+1):
            if(comienzo%divisor==0):
                contador+=1
        if(contador==2):
            primos.append(comienzo)
    print(primos)

    
            