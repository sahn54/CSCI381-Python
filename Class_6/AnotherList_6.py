
# range has to be bigger than the range
# none of the elements are repeats q-p+1 > n
import random


def My_list():
    n = int(input("Please give the size of a list: "))
    p = int(input("enter the starting value:"))
    q = int(input("enter the ending value: "))
    Nlist = []

    for newNum in range(1, n+1):
        newNum = random.randint(p, q)
        if newNum in Nlist:
            continue
        else:
            Nlist.append(newNum)
            continue
    print(Nlist)


My_list()
