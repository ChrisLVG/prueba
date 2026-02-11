#Operando con listas    
def manejar_lista(cantidad):
    lista= []
    for i in range(cantidad):
        valor=(input("introduzca un numero: "))
        lista.append(valor)

    while True:
        print("que desea hacer con la lista?")
        print("1. Mostrar lista")
        print("2. introducir un valor a la lista")
        print("3. introducir varios valores a la lista")
        print("4. eliminar un valor de la lista")
        print("5.ordenar la lista de manera ascendente")
        print("6.invertir la lista")
        print("7.obtener indice de un valor")
        print("8.contar cantidad de elementos de la lista")
        print("9.insertar un elemento en una posicion especifica")
        print("10.limpiar la lista")
        print("11.salir")
        opcion= int(input("ingrese una opcion: "))
        if opcion==1:
            print(lista)
        elif opcion==2:
            valor=(input("introduzca un numero: "))
            lista.append(valor)
        elif opcion==3:
            cantidad= int (input("introduzca la cantidad de numeros que desea"))
            for i in range(cantidad):
                valor=(input("introduzca un numero: "))
                lista.append(valor)
        elif opcion==4:
            valor=(input("introduzca el numero que desea eliminar: "))
            if valor in lista:
                lista.remove(valor)
            else:
                print("el valor no se encuentra en la lista")   
        elif opcion==5:
            try:
                lista.sort()
                print("lista ordenada", lista)
            except Exception as e:
                print("La lista debe contener unicamente numeros para ordenarla de manera ascendente")
        elif opcion==6:
            try:
                lista.reverse()
                print("lista invertida", lista)
            except Exception as e:
                print("La lista debe contener unicamente numeros para invertirla.")
        elif opcion==7:
            valor=(input("introduzca el numero que desea buscar: "))
            if valor in lista:
                indice= lista.index(valor)
                print("el indice del valor es:", indice)
            else:
                print("el valor no se encuentra en la lista")
        elif opcion==8:
            cantidad= len(lista)
            print("la cantidad de elementos en la lista es:", cantidad)
        elif opcion==9:
            valor=(input("introduzca el numero que desea insertar: "))
            posicion= int(input("introduzca la posicion en la que desea insertar el numero: "))
            if posicion < 0 or posicion > len(lista):
                print("posicion invalida")
            else:
                lista.insert(posicion, valor)
        elif opcion==10:
            lista.clear()
            print("lista limpiada")
        elif opcion==11:
            print("saliendo...")
            break
        elif opcion<1 or opcion>11:
            print("opcion invalida, intente de nuevo")
    

