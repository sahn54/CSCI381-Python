# prompt user to input five integers
num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))
num3 = int(input("Enter third integer: "))
num4 = int(input("Enter fourth integer: "))
num5 = int(input("Enter fifth integer: "))


largest = num1
if num2 > largest:
    largest = num2
if num3 > largest:
    largest = num3
if num4 > largest:
    largest = num4
if num5 > largest:
    largest = num5

print("The Largest number is ", largest)
