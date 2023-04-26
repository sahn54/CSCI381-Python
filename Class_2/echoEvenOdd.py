# Write a program that asks the user to enter an integer. Your program should “echo” the input and print
# Even if the number is even and ODD if the number is odd.

number = int(input("Please enter an integer: "))
evenNum = "EVEN"
oddNum = "ODD"


print(evenNum * (number % 2 == 0), oddNum * (number % 2 != 0))


# With if statment
# if number % 2 == 0:
#     print("Even")
# else:
#     print("ODD")

# even == number % 2


# print(number, 'is', number =% 2 + )
