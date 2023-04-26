# The Python “sum” program
print("Welcome to the addition program.")
print("You can enter values for x and y and I will calculate ")
print("and display the sum.")
print()  # prints a blank line
x = input("Please enter a value for x (entering 'done' terminates the program): ")
while x != 'done':  # this a ‘while loop’. It’s an example of “control”.
    x = int(x)
    y = int(input("Please enter a value for y: "))
    sum = x+y
    print("The sum of ", x, " and ", y, " is: ", sum)
    print()
    x = input(
        "Please enter a value for x (entering 'done' terminates the program): ")
print()
print("Thanks for trying our program!")
