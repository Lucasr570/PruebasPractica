import os
clear = lambda : os.system('cls')
clear()

'''Aplicar un descuento dependiendo el precio.
menor o igual que 2000, descuento del 10%
mayor que 2000 y menor o igual a 4000, descuento del 15%
mayor de 4000, descuento del 20%'''

carrito = {
    "tv": 5400,
    "celular": 6300,
    "audifonos": 1100,
    "tablet": 1500,
    "bocina": 600,
    "reloj": 2500,
    "laptop": 10000
}

print("Productos disponibles: ", carrito)
articulo = input("seleccione el producto para determinar el valor con su descuento correspondiente: ")

def calcularDescuento(articulo):
    if carrito[articulo] <= 2000:
        descuento = carrito[articulo] * .10
    elif carrito[articulo] <= 4000:
        descuento = carrito[articulo] * .15
    elif carrito[articulo] > 4000:
        descuento = carrito[articulo] * .20
        
    total = carrito[articulo] - descuento
    print("El producto queda a un valor de: $",total)
    
calcularDescuento(articulo)