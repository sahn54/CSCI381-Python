# Ask the user for three integer n and m and k, where k>m*n
# Create a two dimensional table (list of lists) x of size n*m.
# Populate the list with n*m unique random
# integers in the range 1 through k.
import random


def two_d_table():
    n = int(input("Enter n: "))
    m = int(input("Enter m: "))
    k = int(input("Enter k (where k>m*n): "))

    x = [[0] * m for i in range(n)]

    used_numbers = set()
    for i in range(n):
        for j in range(m):
            while True:
                number = random.randint(1, k)
                if number not in used_numbers:
                    used_numbers.add(number)
                    x[i][j] = number
                    break
    for row in x:
        print(row)


two_d_table()


# # ask the user for three integer n, m, k where k > (m*n)
# # create a two dimensional table (list of lists) x of size n*m
# # populate the list with n*m unique random integers in the range 1 through k

# # 3 x 4 array
# # 3 rows, 4 columns
# # a[c][r]

# # a[1][2]

# # row 0 (array 0): 1, 2, 3, 4
# # row 1 (array 1): 1, 2, 3, 4
# # row 2 (array 2): 1, 2, 3, 4


# # in this problem
# # final answer is gonna be n rows, m columns
# # answer_array
# # answer_array[row][column] =

# from xml.dom.pulldom import CHARACTERS


# def two_dimensional_randoms():
#   n = int(input("enter n: "))
#   m = int(input("enter m: "))
#   k = int(input("enter k: "))
#   if k <= (m*n):
#     print("You have not entered numbers that meet the requirements")
#     return

#   already_used_numbers = set()
#   two_dimensional_solution = [] #technically one-dimensional right now, but we can add lists inside of it
#   #if I add three lists to this [[1,2,3],[2,3,4],[3,4,5]]
#   #by default starts at 0, goes until but not including END_INDEX

#   # loop through all of the rows, one iteration per row
#   for x in range(n):

#     #all the numbers we have so far in the current iteration for the row. clear at the start of the row
#     current_row_numbers = []

#     #loop through as many columns as specified
#     for y in range(m):

#       #we need the number to be unique. start off by assuming it's not unique to just make sure the while loop runs at least once
#       number_unique = False

#       #keep searching until we get a unique number
#       while number_unique is False:

#         #generate a random number on the specified interval
#         random_number = random.randint(1,k)

#         #only allow the program to continue and add the new number if it is not already used
#         if random_number not in already_used_numbers:
#           number_unique = True

#           # add the number we find to the set
#           already_used_numbers.add(random_number)

#       #once we find a unique number, add it to the current_row_numbers
#       current_row_numbers.append(random_number)
#       # looking inside current_row_numbers
#       # after the first iteration [17]
#       # then [17,34]
#       #etc until you finish going through all the columns

#     #when a full row is finished, add it to the two_dimensional_solution
#     two_dimensional_solution.append(current_row_numbers)
#     #what this will look like as it grows:
#     #it will start off empty []
#     # [[17,34]] [] -> add to that list [17,34] which is being considered to an element
#     # on the second iteration
#     #[[17,34],[18,22]] -> add to the list [18,22]
#     #etc until you finish filling up all the rows

#   print(two_dimensional_solution)


# two_dimensional_randoms()
