import Clases.Personaje as p    
personajes={}
combinaciones={}
while True:
    print("Bienvenido al juego de combinacion de personajes")
    print("Crea tu personaje combinando las habilidades de dos personajes diferentes")
    print("Selecciona una opcion")
    print("1.crear personaje")
    print("2.borrar personaje")
    print("3.combinar personajes")
    print("4.mostrar un los personajes")
    print("5.mostrar rodos personajes")
    print("6.mostrar combinacion de personajes")
    print("7.mostrar todas las combinaciones de peronajes")
    print("8.salir")
    opcion= int(input("ingrese una opcion: "))
    if(opcion==1):
        nombre=input("ingrese el nombre del personaje: ")
        fuerza=int(input("ingrese la fuerza del personaje: "))
        velocidad=int(input("ingrese la velocidad del personaje: "))
        personajes[nombre]=[fuerza,velocidad]
    elif(opcion==2):
        if(len(personajes)==0):
            print("no hay personajes para borrar")
        else:
            nombre=input("ingrese el nombre del personaje a borrar: ")
            if nombre in list(personajes.keys()):
                del personajes[nombre]
                print("personaje borrado")
            else:
                print("el personaje no existe")
    elif(opcion==3):
        if len(personajes)<2:
            print("no hay suficientes personajes para combinar")
        else:
            personaje1=input("ingrese el nombre del primer personaje: ")
            personaje2=input("ingrese el nombre del segundo personaje: ")
            if personaje1 in personajes and personaje2 in list(personajes.keys()):
                personaje1=p.Personaje(personaje1, personajes[personaje1][0],personajes[personaje1][1])
                personaje2=p.Personaje(personaje2, personajes[personaje2][0],personajes[personaje2][1])
                combinacion=personaje1+personaje2
                combinaciones[combinacion.nombre]=[combinacion.fuerza, combinacion.velocidad]
                print("combinacion creada")
            else:
                print("uno o ambos personajes no existen")
    elif(opcion==4):
        nombre=input("ingrese el nombre del personaje a mostrar: ")
        if nombre in personajes:
            print(f"Personaje: {nombre}, Fuerza: {personajes[nombre][0]}, Velocidad: {personajes[nombre][1]}")
        else:
            print("el personaje no existe")
    elif(opcion==5):
        if len(personajes)==0:
            print("no hay personajes para mostrar")
        else:
            print("----- Personajes -----")
            print(personajes)
    elif(opcion==6):
        nombre=input("ingrese el nombre de la combinacion a mostrar: ")
        if nombre in combinaciones:
            print(f"Combinacion: {nombre}, Fuerza: {combinaciones[nombre][0]}, Velocidad: {combinaciones[nombre][1]}")
        else:
            print("la combinacion no existe")
    elif(opcion==7):
        if len(combinaciones)==0:
            print("no hay combinaciones para mostrar")
        else:
            print("----- Combinaciones -----")
            print(combinaciones)
    elif(opcion==8):
        print("gracias por jugar")
        break
    elif(opcion<1 or opcion>8):
        print("opcion no valida")