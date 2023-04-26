# def is_prime(x):

# for x in range(1, x, 2):
#     isPrime = True
#     for y in range(2, int(x ** (1/2)) + 1):
#         if x % y == 0:
#             isPrime = False
#     if isPrime:
#         print(x, end=' ')

# is_prime(5)


def is_prime():
    f = int(input("Enter First int: "))
    l = int(input("Enter last int: "))
    for x in range(f, l+1):
        if x >= 2:
            is_prime = True
            for y in range(2, int(x**(0.5))+1):
                if x % y == 0:
                    is_prime = False
                    break
            if is_prime:
                print(x, end=",")


is_prime()
