def generate_base_eight(n):
    num = 0

    for i0 in range(8):
        for i1 in range(8):
            for i2 in range(8):
                for i3 in range(8):
                    for i4 in range(8):
                        for i5 in range(8):
                            for i6 in range(8):
                                for i7 in range(8):
                                    q = [i0, i1, i2, i3, i4, i5, i6, i7]
                                    num += 1
                                    if num == n+1:
                                        print(q)


# Write a function get_num(n) which returns a list of length 8 representing the base eight representation
# of the decimal number n.
n = int(input("Enter n: "))
result = generate_base_eight(n)


# def get_num(n):
#     q = [0] * 8
#     i = 7
#     while n > 0:
#         q[i] = n % 8
#         n //= 8
#         i -= 1
#     return q
