print("What is your age?")
age = int(input(""))

if age > 18:
    if age > 60:
        print("Senior Citizen")
    else:
        print("Adult")
else:
    if age < 13:
        print("Child")
    elif 13 <= age <= 18:
        print("Teenager")