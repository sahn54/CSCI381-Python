# Learning  if statements
# Problem:
# • If n is in the range 1-10, print the color is red!
# • If n is in the range 1-10, print the color is red!
# • If n is in the range 11-20, print the color is blue!
# • If n is in the range 21-30, print the color is green!
# • If the number entered is none of those, print ERROR


# Problem:
# Write a program that inputs three different integers and prints out the largest of the three.
# Answer:

num1 = int(input("Enter an integer: "))
num2 = int(input("Enter another integer: "))
num3 = int(input("Enter another integer: "))

largest = max(num1, num2, num3)

print("The largest number is", largest)
