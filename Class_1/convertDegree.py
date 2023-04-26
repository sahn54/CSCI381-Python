
# Problem: write a program to ask the user for the temperature in Fahrenheit and print out the
# resulting temperature in centigrade. The formula is:

print("Covert Fahrenheit to Celsius")
value = input("Please enter a temperture: ")
finalValue = (int(value) - 32) * (5/9)

print("Covert " + value + "degrees Fahrenheit to degrees Celsius: " +
      str(int(finalValue)) + " C")
