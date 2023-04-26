# Generate and print all prime numbers between 1 and 100.


for x in range(1, 100, 2):
    isPrime = True
    for y in range(2, int(x ** (1/2)) + 1):
        if x % y == 0:
            isPrime = False
    if isPrime:
        print(x, end=' ')
