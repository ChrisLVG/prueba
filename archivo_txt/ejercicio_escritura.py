lista1=["Christian", "Emerlinda", "Elianet","Erick","Henry"]
lista2=["Mendez", "Gomez", "Perez","Rodriguez","Garcia"]
with open("archivo_txt\\archivo.txt", "w") as archivo:
    archivo.write("Nombres y Apellidos:\n")
    for nombre, apellido in zip(lista1, lista2):
        archivo.write(f"{nombre} {apellido}\n")
archivo.close()
