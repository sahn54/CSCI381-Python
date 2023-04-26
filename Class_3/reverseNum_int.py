# Write a program that inputs a three digit integer n (no zero in the units position) and returns the digits
# of n in reverse order. Your program should reject (politely) any input not in the appropriate range.
# For example if you enter the integer 123, the program should output the digits 321 one next to the
# other.
# Answer:

number = int(input("Enter a number: "))
num = number
a = number % 10
number //= 10
b = number % 10
number //= 10
c = number

print(a, b, c, sep='',  end='')


# Problem:
# Write a program that inputs a three digit integer n (no zero in the units position) and returns the
# integer made up of the digits of n in reverse order. Your program should reject (politely) any input not
# in the appropriate range.
# For example if you enter the integer 123, the program should output the integer 321 (not just
# Answer:
print("\n")
number = int(input("Enter a number: "))

num = number
a = number % 10
number //= 10
b = number % 10
number //= 10
c = number

d = a * 100 + b * 10 + c
print(d)
