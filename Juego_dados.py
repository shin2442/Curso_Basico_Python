import random

def print_dice(num):
    if num == 1:
        print("|     |\n|  *  |\n|     |")
    if num == 2:
        print("|*    |\n|     |\n|    *|")
    if num == 3:
        print("|*    |\n|  *  |\n|    *|")
    if num == 4:
        print("|*   *|\n|     |\n|*   *|")
    if num == 5:
        print("|*   *|\n|  *  |\n|*   *|")
    if num == 6:
        print("|* * *|\n|     |\n|* * *|")

while True:
    pregunta = input("¿Quieres tirar un dado?\n\t(si)(no): ")
    if pregunta == "si":
        num = random.randint(1, 6)
        print_dice(num)
    elif pregunta == "no":
        print("Está bien :(, que tengas un buen día.")
        break
    else:
        print("Por favor, responde con 'si' o 'no'.")
