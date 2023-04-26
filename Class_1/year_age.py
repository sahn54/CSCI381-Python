# Problem: Write a program to ask the user their age in years
# and have the program tell them their age in minutes. Don't worry about leap years.

age = int(input("What is you age? "))
yearIndays = age * 365
yearinMin = age * 365 * 24 * 60
print(
    f"Your age is {age} and you are {str(yearIndays)} days or {str(yearinMin)} minutes old.")
