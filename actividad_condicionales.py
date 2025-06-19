#solicitar informacion
nombre = input("Ingrese el nombre del cliente: ")
productos = {}
while True:
    producto = input("Ingrese el nombre del producto (o 'fin' para terminar): ")
    if producto.lower() == 'fin':
        break
    try:
        precio = float(input(f"Ingrese el precio de '{producto}': "))
        cantidad = int(input(f"Ingrese la cantidad de '{producto}': "))
    except ValueError:
        print("Precio o cantidad inválidos. Intente de nuevo.")
        continue
    productos[producto] = {'precio': precio, 'cantidad': cantidad}

valor_compra = sum(info['precio'] * info['cantidad'] for info in productos.values())
#Estableces condiciones
if valor_compra < 80:
    print(f'Hola, {nombre}. El valor a pagar es: ${valor_compra:.2f}')
elif 80 <= valor_compra < 150:
    descuento = 0.1
    precio_final = valor_compra - (valor_compra * descuento)
    print(f'Compra sin descuento: {valor_compra:.2f}. \t Compra con descuento: {precio_final:.2f}')
elif 150 <= valor_compra <= 300:
    descuento = 0.15
    precio_final = valor_compra - (valor_compra * descuento)
    print(f'Compra sin descuento: {valor_compra:.2f}. \t Compra con descuento: {precio_final:.2f}')
elif 300 <= valor_compra < 500:
    descuento = 0.2
    precio_final = valor_compra - (valor_compra * descuento)
    print(f'Compra sin descuento: {valor_compra:.2f}. \t Compra con descuento: {precio_final:.2f}')
else:
    print(f'Hola, {nombre}. El valor a pagar es: ${valor_compra:.2f}')