# Problem:
# Write a program that asks the user for a positive integer n. Calculate and print the sum of the
# integers 1 through n.
# Answer:
i = 1
num = int(input("Enter a positive integer: "))

sum = 0
while i <= num:
    sum += i
    i += 1
print(sum)
