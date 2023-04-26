# print(f"{convert(6, 2)}")


def convert(num, base):
    area = " "
    while num > 0:
        remainder = num % base
        num //= base
        area += str(remainder)
    return (area[::-1])


print(convert(29, 3))
