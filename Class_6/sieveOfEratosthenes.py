def seiveOfEratosthenes(number):
    mylist = []
    p = 2
    num = 0

    for i in range(100+1):
        mylist.append(i)

    primes = [2]

    print(mylist)

    #    if is_prime:
    #         print("It's a prime number.")
    #     else:
    #         print("It's not a prime number.")
    # # if output is a float number or negitive
    # else:
    #     print("It's not a prime number.")


n = int(input("Check this number: "))
seiveOfEratosthenes(number=n)
