#Diccionario
inventario = {}

#funcion agregar producto
def agregar_producto():
    nombre=input("Ingrese el nombre del producto: ").strip().lower()
    if nombre in inventario:
        print("El producto ya existe en el inventario. Se actualizara la cantidad.")
        cantidad=int(input("Ingrese la cantidad adicional: "))
        inventario[nombre]["cantidad"]+= cantidad
    else:
        cantidad=int(input("Ingrese la cantidad inicial del producto: "))
        precio=float(input("Ingrese el precio del producto: "))
        inventario[nombre]={"cantidad":cantidad, "precio":precio}
    print(f"Producto'{nombre}'agregado/actualizado con exito.")

#funcion consultar producto
def consultar_producto():
    nombre=input("Ingrese el nombre del producto: ").strip().lower()
    if nombre in inventario:
        print(f"\nProducto: {nombre}")
        print(f"Cantidad: {inventario[nombre]['cantidad']}")
        print(f"Precio: {inventario[nombre]['precio']}\n")
    else:
        print(f"El producto '{nombre}' no está en el inventario.\n")

#funcion mostrar inventario
def mostrar_inventario():
    if inventario:
        print("\nInventario completo:")
        for nombre, datos in inventario.items():
            print(f"Producto: {nombre}, Cantidad: {datos['cantidad']}, Precio: {datos['precio']}\n")
    else:
        print("El inventario está vacío.\n")

#funcion realizar compra
def realizar_compra():
    nombre = input("Nombre del producto a comprar: ").strip().lower()
    cantidad = int(input("Cantidad a comprar: "))
    if nombre in inventario and inventario[nombre]['cantidad'] >= cantidad:
        inventario[nombre]['cantidad'] -= cantidad
        total = cantidad * inventario[nombre]['precio']
        print(f"Compra realizada. Total a pagar: ${total:.2f}\n")
    else:
        print("No hay suficiente stock o el producto no está en el inventario.\n")
        
#mostrar menu
def menu():
    """Función principal para manejar el menú"""
    while True:
        print("\nMenú de Gestión de Inventario")
        print("1. Agregar producto")
        print("2. Consultar producto")
        print("3. Mostrar inventario")
        print("4. Realizar compra")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            consultar_producto()
        elif opcion == "3":
            mostrar_inventario()
        elif opcion == "4":
            realizar_compra()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente nuevamente.")

# Ejecutar el programa
menu()