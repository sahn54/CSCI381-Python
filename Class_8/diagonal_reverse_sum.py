def sum_value(x):
    diagonal_sum = 0
    n = len(x)
    for i in range(n):
        j = n - i - 1
        diagonal_sum += x[i][j]
    return diagonal_sum


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

diagonal_sum = sum_value(matrix)

print(diagonal_sum)
