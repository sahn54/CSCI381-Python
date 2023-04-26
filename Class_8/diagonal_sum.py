# Problem:
# Write a function to calculate and return the sum of all the elements on the “main diagonal” of the
# square two dimensional list x passed to it as an argument. This is the diagonal going from the upper left
# to the bottom righ


def sum_value(x):
    diagonal_sum = 0
    # for i in range(-1, len(x)-1, -1):
    for i in range(len(x)):
        diagonal_sum += x[i][i]
    return diagonal_sum


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

diagonal_sum = sum_value(matrix)

print(diagonal_sum)
