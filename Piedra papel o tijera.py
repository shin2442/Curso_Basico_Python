print("Bienvenido, juguemos al juego de Piedra, Papel o Tijera\n Escoje una opcion: Piedra, Papel o Tijera")
import random
opciones=["piedra","papel","tijera"]
jugador=input("Tu elecion: ").lower()
if jugador not in opciones:
    print("Opcion no valida. Intenta de nuevo")
else:
    computador =random.choice(opciones)
    print("La computadora eligio:",computador)
if jugador == computador:
    print("¡Es un empate!")
elif (jugador == "piedra" and computador == "tijera") or \
    (jugador == "papel" and computador == "piedra")or \
    (jugador == "tijera" and computador == "papel"):
    print("¡Ganaste!")
else:
    print("¡Perdiste!")
