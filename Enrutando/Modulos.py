from funciones_matematicas import calculadora_palabras as palabaras, Tabla_multiplicacion,Calcular_precio_compra,ejercicio_numeros_primos as primos
print("Que ejercicio queres probar?")
print("1. Calculadora palabras")
print("2. Tabla de multiplicar")
print("3. Calcular precio compra")
print("4. Numeros primos")
opcion=int(input("Ingresa el numero del ejercicio que quieres probar: "))
if opcion==1:
    print(f"Ejercicio calculadora palabras: {palabaras.numero_palabras('hola mundo como estas')}")
if opcion==2:
    intro=int(input("ingresa el numero para mostrar su tabla de multiplicar: "))
    print(f"Ejercicio tabla multiplicar con el {intro}: {Tabla_multiplicacion.tabla_multiplicar(intro)}")
if opcion==3:
    print(f"Ejercicio calcular precio compra: {Calcular_precio_compra.main()}")
if opcion==4:
    rango=int(input("ingresa el rango para mostrar los primos : "))
    print(f"Ejercicio numeros primos hasta el {rango}: {primos.numeros_primos(rango)}")