def registrar_usuario():
    nombre = input("¿Cuál es tu nombre? ").strip().capitalize()
    opciones = ["S", "M", "L", "XL"]
    talla = input("¿Cuál es tu talla de camiseta? (S, M, L, XL) ").strip().upper()

    if talla not in opciones:
        print("La opción no es válida.")
    else:
        with open("registro_camisetas.txt", "a") as archivo:
            archivo.write(f"{nombre}, {talla}\n")
        print("Usuario registrado correctamente.")

    

def ver_registros():
    """Función para mostrar los registros almacenados"""
    try:
        with open("registro_camisetas.txt", "r") as archivo:
            contenido = archivo.readlines()

        if not contenido:
            print("No hay registros aún.")
        else:
            print("\nRegistros de camisetas:")
            for linea in contenido:
                print(linea.strip()) 
    except FileNotFoundError:
        print("El archivo de registros no existe. Agregue un registro primero.")

def menu():
    """Función para mostrar el menú de opciones"""
    while True:
        print("\n--- Registro de Camisetas ---")
        print("1. Registrar usuario")
        print("2. Ver registros")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            ver_registros()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

# Ejecutar el menú
menu()