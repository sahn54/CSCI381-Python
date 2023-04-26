# Write a program for loops to print the following:

# (1,1) (1,2) (1,3)


for x in range(1, 5, 1):
    for y in range(1, 5, 1):
        print(f"( {x} , {y} )", end=" ")
    print()
