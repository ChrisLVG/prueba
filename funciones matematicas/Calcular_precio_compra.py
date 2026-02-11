# Calcula el precio total de una compra de un producto, teniendo en cuenta que el usuario deposita el nombre del producto, la cantidad comprada y el precio. Se debe de mostrar un resumen de la compra al final.
def calcular_precio_total(precio, cantidad):
    return precio * cantidad
def main():
    producto = input("Ingresa el nombre del producto: ")
    precio= float(input("Ingresa el precio del producto: "))
    cantidad = int(input("Ingresa la cantidad comprada: "))
    if precio <=0 or cantidad <=0:
        print("El importe introducido no es correcto")
        main()
    print("Resumen de la compra:")
    print("Producto:", producto)
    print("Precio unitario:", precio)
    print("Cantidad comprada:", cantidad)
    print("Precio total:", calcular_precio_total(precio,cantidad))
    print("Impuesto sobre ventas (21%):", calcular_precio_total(precio,cantidad) * 0.21)
main()