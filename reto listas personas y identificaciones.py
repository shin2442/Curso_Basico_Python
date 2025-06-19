personas = []
identificaciones = []

def agregar_nombre(nombre):
    personas.append(nombre)

def agregar_identificacion(identificacion):
    identificaciones.append(identificacion)

def mostrar_personas():
    for i in range(len(personas)):
        print(f"Nombre: {personas[i]}\nIdentificación: {identificaciones[i]}")

while True:
    nombre = input("Ingrese el nombre de la persona o 'salir' para terminar: ")
    if nombre.lower() == 'salir':
        break
    identificacion = input("Ingrese la identificación de la persona: ")
    agregar_nombre(nombre)
    agregar_identificacion(identificacion)

print("\nPersonas guardadas:")
mostrar_personas()
