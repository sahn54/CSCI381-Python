# Write a program to ask the user their age in years. Your program should calculate and print their age in seconds.

# One way to write:
# age = input("How old are you? ")
# second = int(age) * 365 * 24 * 60 * 60
# print("You are " + str(second) + " seconds old.")

age_years = int(input("How old are you? "))
age_seconds = age_years * 365 * 24 * 60 * 60
print("You are", age_seconds, "seconds old.")
