texto= str(input("Ingrese el texto para calcular la cantidad de palabras: "))
palabras= texto.split()#convierto el texto en una lista de palabras separadas por espacios
print("Cantidad de palabras en el texto: ", len(palabras))
print("tardarias aproximadamente ", len(palabras)/2, "segundos en decir esta frase")
if len(palabras)/2 > 60:
    print("para flaco tampoco te pedi un testamento")
print("Dalto tardaria aproximadamente ", round(len(palabras)/2.6, 1), "segundos en decir esta frase")
