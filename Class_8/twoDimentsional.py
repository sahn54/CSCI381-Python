
# ask the user for three integer n, m, k where k > (m*n)
# create a two dimensional table (list of lists) x of size n*m
# populate the list with n*m unique random integers in the range 1 through k

# 3 x 4 array
# 3 rows, 4 columns
# a[c][r]

# a[1][2]

# row 0 (array 0): 1, 2, 3, 4
# row 1 (array 1): 1, 2, 3, 4
# row 2 (array 2): 1, 2, 3, 4


# in this problem
# final answer is gonna be n rows, m columns
# answer_array
# answer_array[row][column] =

# from xml.dom.pulldom import CHARACTERS


# Problem:
# Ask the user for three integer n and m and k, where k>m*n.
# Create a two dimensional table (list of lists) x of size n*m. Populate the list with n*m unique random
# integers in the range 1through k.


import random


# def two_dimensional_randoms():
#     n = int(input("enter n: "))
#     m = int(input("enter m: "))
#     k = int(input("enter k: "))
#     if k <= (m*n):
#         print("You have not entered numbers that meet the requirements")
#         return

#     already_used_numbers = set()
#     two_dimensional_solution = []

#     for x in range(n):
#         current_row_numbers = []
#         for y in range(m):
#             number_unique = False
#             while number_unique is False:
#                 random_number = random.randint(1, k)
#                 if random_number not in already_used_numbers:
#                     number_unique = True
#                     already_used_numbers.add(random_number)
#             current_row_numbers.append(already_used_numbers)
#         two_dimensional_solution.append(current_row_numbers)
#     print(two_dimensional_solution)


# two_dimensional_randoms()


def twodem():
    n = int(input("Enter n: "))
    m = int(input("Enter m: "))
    k = int(input("Enter k: "))
    while k <= (m*n):
        k = int(input("Please enter again for k:"))
    mylist = []

    mySet = set()
    # create a two deimnesional table x of size n * m
    for i in range(n):
        level2_list = []
        for j in range(m):
            # populate the list with n*m unique randome int range 1 to k
            j = random.randint(1, k)
            if j not in mySet:
                mySet.add(j)
                level2_list.append(j)
        mylist.append(level2_list)
    print(mylist)


twodem()
