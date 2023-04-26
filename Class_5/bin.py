# Just like there are conversions, int, float, str, there is a built-in function called bin. The documentation
# says:
# bin(x)
# Convert an integer number to a binary string

# print(f"{bin(6)}")


def my_bin(num):
    binNum = ""
    while num > 0:
        value = num % 2
        num //= 2
        binNum += str(value)
    return (binNum[::-1])


print(my_bin(14))
