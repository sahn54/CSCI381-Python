# Write a program that asks the user to enter an integer. Your program should “echo” the input and print
# True if the number is even and False if the number is odd.

number = int(input("Please enter an integer: "))
print(bool(number % 2 == 0))


# With if statement:

# if number % 2 == 0:
#     print("True")
# else:
#     print("False")
# while (number % 2 == 0):
#     print("True")
# print("False")

# print(number, bool(not number % 2))
