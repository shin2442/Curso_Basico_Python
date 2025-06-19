print("Welcome to a Student Grade Categorization")
score = int(input("What is your score (0-100)? "))

if score > 50:
    if score > 80:
        print("Excellent")
    else:
        print("Good")
else:
    if score < 30:
        print("Fail")
    elif 30 <= score <= 50:
        print("Needs Improvement")
