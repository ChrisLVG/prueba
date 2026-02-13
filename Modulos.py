print("Que ejercicio queres probar?")
print("1. Calculadora palabras")
print("2. Tabla de multiplicar")
print("3. Calcular precio compra")
print("4. Numeros primos")
opcion=int(input("Ingresa el numero del ejercicio que quieres probar: "))
if opcion==1:
    import funciones_matematicas.calculadora_palabras as palabaras
    intro=("la frase que quiere analizar")
    print(f"Ejercicio calculadora palabras: {palabaras.numero_palabras(intro)}")
if opcion==2:
    import funciones_matematicas.Tabla_multiplicacion as Tabla_multiplicacion
    intro=int(input("ingresa el numero para mostrar su tabla de multiplicar: "))
    print(f"Ejercicio tabla multiplicar con el {intro}: ")
    Tabla_multiplicacion.tabla_multiplicar(intro)
if opcion==3:
    import funciones_matematicas.Calcular_precio_compra as Calcular_precio_compra
    Calcular_precio_compra.main()
if opcion==4:
    import funciones_matematicas.ejercicio_numeros_primos as primos
    rango=int(input("ingresa el rango para mostrar los primos : "))
    print(f"Ejercicio numeros primos hasta el {rango}: ")
    primos.numeros_primos(rango)