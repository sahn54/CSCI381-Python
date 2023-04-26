# Problem:
# Recall the definition of a prime number:
# An integer greater than one is called a prime number if its only positive divisors (factors) are one
# and itself.
# Write a program that inputs a positive integer n and determines if n is prime or composite (i.e.
# not a prime).
# Answer:
# We now look at the second loop structure in Python, the


number = int(input("Enter a prime number: "))

if number > 1:
    while (number % 2) == 0:
        print(number, "is not a prime number.")
        break
    else:
        print(number, "is a prime number.")
elif number == 1:
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")
