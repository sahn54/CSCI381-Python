# Write a program that asks the user for a positive integer n where the right-most digit is not a
# zero. Print out the digits of n from right to left – one next to the other.

number = int(input("Enter a number: "))
sum = 0
while (number > 0):
    sum = sum * 10 + number % 10
    number //= 10
print(sum)
