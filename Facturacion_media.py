# calcular facturacion media
def facturacion_media(facturas):
    total = sum(facturas)
    media = total / len(facturas)
    return media

facturaciones_validas = False
while facturaciones_validas == False:
    facturaciones = input("Introduce las facturaciones separadas por comas: ")
    if facturaciones.strip():
        try:
            facturaciones = [float(x.strip()) for x in facturaciones.split(",")]
            facturaciones_validas = True
        except ValueError:
            print("Error: Asegurese de introducir numeros separados por comas correctamente.")
            facturaciones_validas = False
    else:
        print("No se introdujo ninguna facturación. Intenta de nuevo.")

if facturaciones_validas:
    media = facturacion_media(facturaciones)
    print("La facturación media es:", media)
