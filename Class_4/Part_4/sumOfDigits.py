# Problem:
# Write a function sum_of_digits(n) which returns the sum of the digits of n.

def sum_of_digits(n):
    # Initialize the sum to zero
    digit_sum = 0
    # Convert the integer to a string to access each digit
    str_n = str(n)
    # Iterate over each digit in the string and add it to the sum
    for digit in str_n:
        digit_sum += int(digit)
    # Return the final sum
    return digit_sum


print(sum_of_digits(43))
