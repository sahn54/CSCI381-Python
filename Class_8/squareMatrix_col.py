# Problem:
# Write a function get_col(x,i) which takes a square matrix (=table=list of lists) and returns a list
# containing the ith column of matrix X.
import random

# List Comprehensions version:
# def get_col(x, j):
#     return [x[i][j] for i in range(len(x))]


def get_col(x, j):
    l = []
    for i in range(len(x)):
        l.append(x[i][j])
    return l


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

print(get_col(matrix, 2))
