# Ask the user for two integer n and m where m>n.
# Create a list x of size n. Populate the list with n random integers in the range 1through m
# Modify the answer to the problem above so that all of the integers in list x are unique.
from random import randint


def populate():
    n = int(input("Enter an integer n: "))
    m = int(input("Enter an integer m: "))
    while m <= n:
        m = int(input("Please enter again for m:"))
    mylist = []
    mySet = set()
    # create size n
    for i in range(n):
        i = randint(1, m)
        if i not in mySet:
            mySet.add(i)
            mylist.append(i)
    return mylist


print(populate())
