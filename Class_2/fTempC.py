# Write an assignment statement to convert a floating point number x, to its rounded value y.
# Do this in two ways: (1) without using the built-in “round” function, and (2) once with. Here is how
# the Python documentation describes the round function.
print("Covert Fahrenheit to Celsius")
value = input("Please enter a temperture: ")
finalValue = (int(value) - 32) * (5/9)


print("Covert", value, "degrees Fahrenheit to degrees Celsius:",
      round(finalValue), "C")

# Bankers round - nearest even intagers
# 2.5 -> 2
# 0.5 -> 0


# fahrenheit = int(input("Enter the tempature in fahrenheit: "))
# celsius = (fahrenheit - 32) * (5/9)
# print("The tempature in Celsius is", round(celsius))
