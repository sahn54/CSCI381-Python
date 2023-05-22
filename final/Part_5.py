# ------------------------------------------Set()-----------------------------------------------

# Ask the user for two integer n and m where m>n.
# Create a list x of size n. Populate the list with n random integers in the range 1through m.


from itertools import permutations
import random

# n = int(input("Enter n :"))
# m = int(input("Enter m :"))
# if m <= n:
#     n = int(input("Enter n :"))
#     m = int(input("Enter m :"))

# x = []
# # n is size
# for _ in range(n):
#     random_int = random.randint(1, m)
#     x.append(random_int)

# x = [random.randint(1, m) for _ in range(n)]


# print(x)

# Modify the answer to the problem above so that all of the integers in list x are unique.


# n = int(input("Enter n :"))
# m = int(input("Enter m :"))
# if m <= n:
#     n = int(input("Enter n :"))
#     m = int(input("Enter m :"))

# x = []
# check_num = set()
# # n is size
# while len(x) != n:
#     random_int = random.randint(1, m)
#     if random_int not in check_num:
#         check_num.add(random_int)
#         x.append(random_int)

# print(sorted(x))


# Ask the user for three integer n and m and k, where k>m*n.
# Create a two dimensional table (list of lists) x of size n*m.
# Populate the list with n*m unique random
# integers in the range 1 through k.


# n = int(input("Enter n :"))
# m = int(input("Enter m :"))
# k = int(input("Enter k :"))
# if k <= m*n:
#     k = int(input("Please re-enter k :"))

# x = []
# check_num = set()
# for i in range(n):
#     second = []
#     while len(second) != m+1:
#         random_int = random.randint(1, k)
#         if random_int not in check_num:
#             check_num.add(random_int)
#             second.append(random_int)

#     x.append(sorted(second))


# print(x)


# Write a function get_row(x,i) which takes a square matrix (=table=list of lists) and returns a list
# containing the ith row of matrix X.

# square_matrix = [[1, 2, 3],
#                  [4, 5, 6],
#                  [7, 8, 9]]

# def get_row(x, i):
#     return x[i]

# print(get_row(square_matrix, 1))

# Write a function get_col(x,i) which takes a square matrix (=table=list of lists) and returns a list
# containing the ith column of matrix X.


# def get_col(x, i):
#     new_list = [j[i] for j in x]
#     return new_list


# print(get_col(square_matrix, 1))

# Write a function to calculate and return the sum of all the elements on the “main diagonal” of the
# square two dimensional list x passed to it as an argument. This is the diagonal going from the upper left
# to the bottom right.

# def get_sum(x):
#     my_sum = 0

#     for i in range(len(x)):
#         my_sum += x[i][i]

#     return my_sum


# print(get_sum(square_matrix))


# Like the problem above, calculate and return the diagonal sum, but for the elements along the diagonal
# going from the top right to the lower left.

# def get_sum_reverse(x):
#     my_sum = 0

#     for i in range(len(x)):
#         my_sum += x[i][(len(x)-i) - 1]

#     return my_sum


# print(get_sum_reverse(square_matrix))


# ------------------------------------------List Comprehensions-----------------------------------------------


square_matrix = [[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]]

# Write a function get_col(x,i) which takes a square matrix (=table=list of lists) and returns a list
# containing the items in the ith column of matrix X.


def get_col(x, i):
    return [x[j][i] for j in range(len(x))]

# Write a function sum_col(x,i) which takes a square matrix (=table=list of lists) and the sum of the
# items in the ith column of matrix X. Use a list comprehension.


def get_col_sum(x, i):
    return sum([x[j][i] for j in range(len(x))])  # type: ignore


print(get_col(square_matrix, 1))
print(get_col_sum(square_matrix, 1))


# Write a function diag_diff(x,i) which takes a square matrix (=table=list of lists) and the difference of
# two main diagonals of matrix X. In other words, let d1 be the diagonal of X from upper left to bottom
# right, and d2 to be the diagonal from upper right to lower left. The function returns d1-d2. Use list
# comprehensions.

def diag_diff(x):
    return sum([x[i][i] for i in range(len(x))]) - sum(x[i][len(x)-i-1] for i in range(len(x)))


print(diag_diff(square_matrix))

# Early versions of Python distinguished between int and long. ints were represented natively on the
# hardware and longs were lists of integers. From version 3.0 and on all integer types are represented as
# longs.
# Write a function make_int (x: str) -> list:
# that takes a string of digits and returns a list of those digits. Use a list comprehension.


# def make_int(x: str) -> list:
#     return [int(i) for i in x]


# print(make_int("1234"))


def make_sum(x: str, y: str):
    return sum([int(i) for i in x]) + sum([int(j) for j in y])


# Write a function int_add(x,y) that takes two “integers” as represented above, and returns their sum.
# Note that these “integers” needn’t be the same size. You can simplify your program by padding the shorter one with
# zeros (on the left).
# Note as well, there might be a final carry that will increase the answer by one digit more than the addends.

# def make_int(x:list, y:list) -> list:
#     if len(x) < len(y):
#         x += [0] *(len(y) - len(x))
#     elif len(x) > len(y):
#         y += [0] *(len(x) - len(y))

    # result =

    # return

# print(make_int("1234", "78943"))


# Write a function matrix_add(x,y) that takes two square “matrices” and returns their sum.

matrix1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

matrix2 = [[9, 8, 7],
           [6, 5, 4],
           [3, 2, 1]]


def matrix_add(x, y):
    return [[x[i][j] + y[i][j] for j in range(len(x))] for i in range(len(x))]


print(matrix_add(matrix1, matrix2))

# Write a function matrix_mult(x,y) that takes two square “matrices” and returns their product.


def matrix_mult(x, y):
    return [[sum(x[i][k] * y[k][j] for k in range(len(x))) for j in range(len(x))]for i in range(len(x))]
# first matrix goes by row
# second matrix goes by col
# 1*9 + 2*6 + 3*3 = 30
# 1*8 + 2*5 + 3*2 = 24
# 1*7 + 2*4 + 3*1 = 18

# 4*9 + 5*6 + 6*3 = 66+18 = 84


# print(matrix_mult(matrix1, matrix2))
# [[30, 24, 18], [84, 69, 54], [138, 114, 90]]


# Now, here is a definition: A saddle point in a 2 dimensional square table is an entry in the table whose
# value is the minimum in its row and maximum in its column. In the table below, 0 is a saddle point.
#           |
#           |   <Saddle Point>
#           |
#           |
# -----------------------
#           |
#           |
#           |
#           |


# Write a function to find a saddle point in a 2 dimensional table in any two dimensional square of
# integers, if one exists. If a saddle point was found return a tuple (value, x pos, y pos). If a saddle point
# was not found return “not found"

# we are trying to get the min its row and the max of the col

# return (value, position of x , position of y)
# you compare each col is

def saddle_point(matrix):
    n_row, n_col = len(matrix), len(matrix[0])
    for i in range(n_row):
        min_row = min(matrix[i])
        for j in range(n_col):
            col_max = max(matrix[i][j] for k in range(n_row))
            if matrix[i][j] == min_row and matrix[i][j] == col_max:
                return matrix[i][j], i, j


# def saddle_point(matrix):
#     for i in range(len(matrix)):
#         row = matrix[i]
#         for j in range(len(matrix)):
#             col = [matrix[k][j] for k in range(len(matrix))]
#             if matrix[i][j] == min(row) and matrix[i][j] == max(col):
#                 return (matrix[i][j], min(row), max(col), row, col)
#             else:
#                 return "not found"
new_matrix = [[1, 3, 4],
              [0, 1, 1],
              [-2, 5, 1]]

# new_matrix = [[9, 3, 4],
#               [0, 2, -2],
#               [-2, 5, 7]]


print(saddle_point(new_matrix))


def find_saddle_point(matrix):
    n_rows, n_cols = len(matrix), len(matrix[0])
    for i in range(n_rows):
        row_min = min(matrix[i])
        for j in range(n_cols):
            col_max = max(matrix[k][j] for k in range(n_rows))
            if matrix[i][j] == row_min and matrix[i][j] == col_max:
                return (matrix[i][j], i, j, row_min, col_max)
    return "not found"


print(find_saddle_point(new_matrix))

# ------------------------------------------------------------

# for i0 in range(8):
#     for i1 in range(8):
#         for i2 in range(8):
#             for i3 in range(8):
#                 for i4 in range(8):
#                     for i5 in range(8):
#                         for i6 in range(8):
#                             for i7 in range(8):
#                                 q = [i0, i1, i2, i3, i4, i5, i6, i7]
#                                 print(q)

# Write a function get_num(n) which returns a list of length 8 representing the base eight representation
# of the decimal number n.


# def get_num(n: int) -> list:
#     q = [0] * 8
#     i = 7
#     while n > 0:
#         q[i] = n % 8
#         n //= 8
#         i -= 1
#     return q


# my_input = int(input("Enter n: "))
# print(get_num(my_input))


# -----------------------------------------------------------
# a = [5*[0] for i in range(5)]
# # set up the left and top boundaries of the table (5X5 square array)
# for i in range(5):
#     a[i][0] = 1
#     a[0][i] = 1
# for i in range(1, 5):
#     for j in range(1, 5):
#         a[i][j] = a[i-1][j]+a[i][j-1]


# print(a[4][4])
# -----------------------------------------------------------------------------------------

# eight Queens problem:
# global N
# N = 4


# def solution(board):
#     for i in range(N):
#         for j in range(N):
#             print(board[i][j], end=' ')
#         print()


# def is_safe(board, row, col):
#     pass


def diagonal_threat(q):

    for col in range(7, 0, -1):

        for i in range(col):

            if col-i == abs(q[col]-q[i]):

                return True  # there is a diagonal threat!

    return False


candidates = permutations([0, 1, 2, 3, 4, 5, 6, 7])

count = 0

for p in candidates:

    if diagonal_threat(p):

        continue

    count += 1

    print('Solution number ', count, ': ', p)

    print()
