def numero_palabras(texto):
    palabras= texto.split()#convierto el texto en una lista de palabras separadas por espacios
    print("Cantidad de palabras en el texto: ", len(palabras))
    print("Si dices 2 palabras por segundo tardarias aproximadamente ", len(palabras)/2, "segundos en decir esta frase")
    if len(palabras)/2 > 60:
        print("para flaco tampoco te pedi un testamento")
    print("Si Dalto habla un 30% mas rapido tardaria aproximadamente ", round(len(palabras)/2.6, 1), "segundos en decir esta frase")