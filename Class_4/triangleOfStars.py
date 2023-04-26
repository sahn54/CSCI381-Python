# Write a program that asks the user for a positive integer n. Print a triangle of “stars”( = “*”) like
# in the example below.

edge = int(input("Please enter an integer between 1 and 10: "))
for i in range(0, edge):
    for j in range(0, i+1):
        print("*", end="")
    print(" ")
