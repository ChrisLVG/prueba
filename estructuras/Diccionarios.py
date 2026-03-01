#trabajar con diccionarios en python
mi_diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}
def manejar_diccionario(mi_diccionario):
    while True:
        print("\n=== MENÚ ===")
        print("1. Ver diccionario entero")
        print("2. Ver claves")
        print("3. Ver valores")
        print("4. Agregar nuevo valor")
        print("5. Buscar valor por clave")
        print("6. modificar valor por clave")
        print("7. Limpiar diccionario")
        print("8. Salir")
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            print("Diccionario entero:", mi_diccionario)
        elif opcion == "2":
            print("Claves:", list(mi_diccionario.keys()))
        elif opcion == "3":
            print("Valores:", list(mi_diccionario.values()))
        elif opcion == "4":
            clave = input("Ingresa la clave: ")
            valor = input("Ingresa el valor: ")
            mi_diccionario[clave] = valor
            print("Valor agregado correctamente")
        elif opcion == "5":
            clave = input("Ingresa la clave a buscar: ")
            if clave in mi_diccionario:
                print(f"Valor: {mi_diccionario[clave]}")
            else:
                print("Clave no encontrada")
        elif opcion == "6":
            clave_b = input("Ingresa la clave a modificar: ")
            if clave_b in mi_diccionario:
                for clave, valor in mi_diccionario.items():
                    if clave == clave_b:
                        nuevo_valor = input("Ingresa el nuevo valor: ")
                        mi_diccionario[clave] = nuevo_valor
                        print("Valor modificado correctamente")
            else:
                print("Clave no encontrada")
        elif opcion == "7":
            mi_diccionario.clear()
            print("Diccionario limpiado")
        elif opcion == "8":
            break
        else:
            print("Opción inválida")