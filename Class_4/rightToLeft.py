n = int(input("Enter a positive integer: "))

if n % 10 == 0:
    print("The right-most digit cannot be zero.")
else:
    digits = []
    while n > 0:
        digits.append(n % 10)
        n = n // 10
    digits.reverse()
    print("The digits of the number from right to left are:")
    for digit in digits:
        print(digit, end="")
