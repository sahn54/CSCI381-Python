# Write a program that asks the user to enter two integers. Your program should:
# • “Store” the values entered in variables a and b.
# • “Print a and b.
# • “Swap” the values in a and b, so that what was in a is now in b and vice versa.
# • Print a and b. At this point the values should be the reverse of what you printed above

num1 = int(input("Please enter first integers: "))
num2 = int(input("Please enter second integers: "))

print("Your first integer is:", num1, "Your second integer is:", num2)

num3 = num1
num1 = num2
num2 = num3


print("After the swap: Your first integer is:",
      num1, "Your second integer is:", num2)
