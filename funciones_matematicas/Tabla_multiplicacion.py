# A partir de un numero mostrar su tabla de multiplicar 
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(numero, "x", i, "=", numero*i)