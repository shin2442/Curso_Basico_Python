import random
while True:
    pregunta=input("Quieres tirar un dado?\n\t(si)(no)")
    if pregunta=="si":
        num=random.randint(1,6)
        if num==1:
                print("|\t\t|\n|\t*\t|\n|\t\t|")
        if num==2:
                print("|*\t|\n|\t\t|\n|\t*|")
        if num==3:
                print("|*\t\t|\n|\t*\t|\n|\t\t*|")
        if num==4:
                print("|*\t*|\n|\t|\n|*\t*|")   
        if num==5:
                print("|*\t*|\n|\t*\t|\n|*\t*|")
        if num==6:
                print("|***|\n|***|\n|***|")
        break
else:
    print("Esta bien :(, que tengas un buen dia")