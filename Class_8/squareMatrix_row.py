# Problem:
# Write a function get_row(x,i) which takes a square matrix (=table=list of lists) and returns a list
# containing the ith row of matrix X.
import random


def get_row(x, i):
    return x[i]


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]


print(get_row(matrix, 1))
