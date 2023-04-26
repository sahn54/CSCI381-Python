# Problem:
# Write a program, using for loops, to generate the following output. (68)
# Might be in the exam (!!!!)

for x in range(9):
    print(" " * x, end="")
    for j in range(1+x, 10):
        print(j, end="")
    for j in range(8, 0+x, -1):
        print(j, end="")
    print()
