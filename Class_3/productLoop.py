# Write a program that asks the user for a positive integer n. Calculate and print the product of the
# integers 1 through n.


i = 1
num = int(input("Enter a positive integer: "))

product = 1
while i <= num:
    product *= i
    i += 1
print(product)
