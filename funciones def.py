import random

def obtener_eleccion_usuario():
    opciones=["piedra","papel","tijera"]
    eleccion=input("Tu elecion: ").lower()
    while eleccion not in opciones:
    print("Opcion no valida. Intenta de nuevo").lower()
    opciones=["piedra","papel","tijera"]
    return opciones

def obtener_eleccion_computador():
    opciones=["piedra","papel","tijera"]
    return random.choice(opciones)

def ganador(usuario, computador):
    if usuario == computador:
        return "¡Empate!"
    elif (usuario == "piedra" and computador == "tijeras") or \
         (usuario == "papel" and computador == "piedra") or \
         (usuario == "tijeras" and computador == "papel"):
        return "¡Ganaste!"
    else:
        return "¡Perdiste!"
    
    
def jugar():
    print("Bienvenido, juguemos al juego de Piedra, Papel o Tijera\n Escoje una opcion: Piedra, Papel o Tijera")
    usuario=obtener_eleccion_usuario()
    computador=obtener_eleccion_computador()
    print(f"La computadora eligio: {computador}")
    resultado=ganador(usuario, computador)
    print(resultado)
    
if __name__ == "__main__":
    jugar()