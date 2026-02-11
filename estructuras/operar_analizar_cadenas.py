cadena= input("Ingrese una cadena de texto: ")
while True:
    print("Seleccione una opción:")
    print("1. Contar caracteres")
    print("2.Econtrar caracter especifico")
    print("3.Econtrar caracter especifico")
    print("4.Econtrar el indice de un caracter especifico")
    print("5.verificar si la cadena entera es numerica")
    print("6.verificar si la cadena entera es alfanumerica")
    print("7.Contar conincidencias de un caracter especifico")
    print("8.Contar caracteres de la cadena")
    print("9.Verificar si la cadena inicia con un texto especifico")
    print("10.Verificar si la cadena termina con un texto especifico")
    print("11.Reemplazar un caracter especifico por otro")
    print("12.Separar la cadena en una lista de subcadenas")
    print("13.Convertir a mayúsculas") 
    print("14.Convertir a minúsculas")
    print("15.Verificar si es un palíndromo")
    print("16.Introducir nueva cadena")
    print("17. Salir")
    opcion = int(input("Ingrese el número de la opción deseada: "))
    if opcion == 1:
        print("Número de caracteres:", len(cadena))
    elif opcion == 2:
        caracter = input("Ingrese el caracter a encontrar: ")
        if caracter in cadena:
            print(f"El caracter '{caracter}' se encuentra en la cadena.")
        else:
            print(f"El caracter '{caracter}' no se encuentra en la cadena.")
    elif opcion == 3:
        caracter = input("Ingrese el caracter a encontrar: ")
        indice = cadena.find(caracter)
        if indice != -1:
            print(f"El caracter '{caracter}' se encuentra en la posición {indice}.")
        else:
            print(f"El caracter '{caracter}' no se encuentra en la cadena.")
    elif opcion == 4:
        caracter = input("Ingrese el caracter a encontrar: ")
        indice = cadena.index(caracter) if caracter in cadena else -1
        if indice != -1:
            print(f"El caracter '{caracter}' se encuentra en la posición {indice}.")
        else:
            print(f"El caracter '{caracter}' no se encuentra en la cadena.")
    elif opcion == 5:
        if cadena.isdigit():
            print("La cadena es numérica.")
        else:
            print("La cadena no es numérica.")
    elif opcion == 6: 
        if cadena.isalnum():
            print("La cadena es alfanumérica.")
        else:
            print("La cadena no es alfanumérica.")
    elif opcion == 7:
        caracter = input("Ingrese el caracter a contar: ")
        if caracter in cadena:
            print(f"El caracter '{caracter}' aparece {cadena.count(caracter)} veces en la cadena.")
        else:
            print(f"El caracter '{caracter}' no se encuentra en la cadena.")
    elif opcion == 8:
        print("Número de caracteres:", len(cadena)) 
    elif opcion == 9:
        texto = input("Ingrese el texto para verificar el inicio: ")
        if cadena.startswith(texto):
            print(f"La cadena inicia con '{texto}'.")
        else:
            print(f"La cadena no inicia con '{texto}'.")
    elif opcion == 10:
        texto = input("Ingrese el texto para verificar el final: ")
        if cadena.endswith(texto):
            print(f"La cadena termina con '{texto}'.")
        else:
            print(f"La cadena no termina con '{texto}'.")
    elif opcion == 11:
        caracter_viejo = input("Ingrese el caracter a reemplazar: ")
        caracter_nuevo = input("Ingrese el nuevo caracter: ")
        if caracter_viejo not in cadena:
            print(f"El caracter '{caracter_viejo}' no se encuentra en la cadena.")
        else:
            nueva_cadena = cadena.replace(caracter_viejo, caracter_nuevo)
            print("Cadena modificada:", nueva_cadena)
    elif opcion == 12:
        separador = input("Ingrese el separador para dividir la cadena: ")
        subcadenas = cadena.split(separador)
        print("Lista de subcadenas:", subcadenas)
    elif opcion == 13:
        print("Cadena en mayúsculas:", cadena.upper())
    elif opcion == 14:
        print("Cadena en minúsculas:", cadena.lower())
    elif opcion == 15:
        cadena_sin_espacios = cadena.replace(" ", "").lower()
        if cadena_sin_espacios == cadena_sin_espacios[::-1]:
            print("La cadena es un palíndromo.")
        else:
            print("La cadena no es un palíndromo.")
    elif opcion == 16:
        cadena = input("Ingrese una nueva cadena de texto: ")
    elif opcion == 17:
        print("Saliendo del programa.")
        break
    elif opcion >17:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 17.") 