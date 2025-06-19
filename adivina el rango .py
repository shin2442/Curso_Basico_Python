import random

computer_num = random.randint(1, 100)
attempts = 8

print("¡Bienvenido al juego de adivinanza de números!\nTienes 8 oportunidades para adivinar un número entre 1 y 100.")

while attempts > 0:
    guess = int(input(f"Intento {9 - attempts}: Ingresa tu suposición: "))

    if guess == computer_num:
        print("¡Felicidades, Ganaste😊")
        break
    elif guess < computer_num:
        print("\nEl numero es mas alto. Inténtalo de nuevo.")
    else:
        print("\nEl numero es mas bajo. Inténtalo de nuevo.")

    attempts -= 1

    if attempts == 0:
        print(f"\nPerdiste 😭, has utilizado todos tus intentos. \nEl número era {computer_num}.")
        break
