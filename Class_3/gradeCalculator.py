grade = int(input("Please enter your grade: "))


if 100 >= grade >= 90:
    print("you got an A")
elif 89 >= grade >= 80:
    print("you got an B")
elif 79 >= grade >= 70:
    print("you got an C")
elif 69 >= grade >= 60:
    print("you got an D")
elif grade < 60:
    print("You got an F")
else:
    print("Score out of the range.")
