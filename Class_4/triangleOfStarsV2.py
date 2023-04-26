# Write a program that asks the user for a positive integer n. Print a triangle of “stars”( = “*”) like
# Upside down

# edge = int(input("Please enter an integer between 1 and 10: "))
# for i in range(edge, 0, -1):
#     for j in range(i, 0, -1):
#         print("*", end="")
#     print(" ")
num = int(input("Please enter an integer between 1 and 10: "))
i = num
while i >= 1:
    j = 1
    while j <= i:
        print("*", end="")
        j += 1
    print(" ")
    i -= 1
