personas = []
identificaciones =[]

def agregar_nombre():
    personas.append({'nombre': nombre})

def agregar_identificacion():
    identificaciones.append({'identificacion': identificacion})

def mostrar_personas():
    for persona in personas:
        print(f"Nombre: {persona['nombre']}\n Identificación: {identificaciones['identificacion']}")

while True:
    nombre = input("Ingrese el nombre de la persona o 'salir' para terminar: ")
    if nombre.lower() == 'salir':
        break
    identificacion = input("Ingrese la identificación de la persona: ")
    agregar_nombre(),agregar_identificacion()


print("\nPersonas guardadas:")
mostrar_personas()
