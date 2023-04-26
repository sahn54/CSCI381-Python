# Problem:
# Write a program to request and validate a password from your user. A valid password
# will be any two digit integer, both digits of which are even.
# Give the user three chances to enter a correct password.
# • At each incorrect attempt, print “Invalid password. Try again”
# • If the password entered is correct print “Correct! You may access the system.” Exit the
# program.
# • If the password entered is incorrect print “Too many invalid attempts. Please try again
# later.”


password = int(input("please enter a password"))
num = password
a = num % 10
num //= 10
b = num % 10
num //= 10

d = a == b

while password == a:
    print("Invaild password. Try again")
    print("Correct! You may access the system.")
    print("Too many invaild attempts, Please try again later.")
