import random

def jugar():
    opciones = ["piedra", "papel", "tijera"]
    jugador = input("Tu elección (piedra, papel o tijera): ").lower()
    if jugador not in opciones:
        print("Opción no válida. Intenta de nuevo.")
        return

    computador = random.choice(opciones)
    print("La computadora eligió:", computador)
    
    if jugador == computador:
        print("¡Es un empate!")
    elif (jugador == "piedra" and computador == "tijera") or \
         (jugador == "papel" and computador == "piedra") or \
         (jugador == "tijera" and computador == "papel"):
        print("¡Ganaste!")
    else:
        print("¡Perdiste!")

def main():
    print("Bienvenido, juguemos al juego de Piedra, Papel o Tijera\n")
    while True:
        jugar()
        jugar_otra_vez = input("¿Quieres jugar otra vez? (sí/no): ").lower()
        if jugar_otra_vez != "si" and jugar_otra_vez != "sí":
            print("¡Gracias por jugar! Hasta luego.")
            break

if __name__ == "__main__":
    main()
