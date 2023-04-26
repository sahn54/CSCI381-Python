import random

# Step 1: Make sure that the number of columns in the 1st matrix equals the number of rows in the 2nd matrix (compatibility of matrices).
# Step 2: Multiply the elements of ith row of the first matrix by the elements of jth column in the second matrix and add the products. This would the element that is in the ith row and jth column of the resultant matrix.
# Step 3: Place the added products in the respective positions.


def matrix_mult(x, y):
    newMatrix = [[0 for j in range(len(y[0]))]for i in range(len(x))]

    for i in range(len(x)):  # get matrix (3X3)
        for j in range(len(y[0])):
            for k in range(len(y)):
                newMatrix[i][k] += x[i][k] * y[k][j]

    for row in newMatrix:
        print(row)


matrix1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

matrix2 = [[4, 2, 2],
           [2, 3, 6],
           [3, 5, 7]]

matrix_mult(matrix1, matrix2)

# To start coding the matrix_mult function to compute newMatrix, you need to first understand how matrix multiplication works.

# Matrix multiplication is defined as the product of the elements of a row in the first matrix with the corresponding elements in a column of the second matrix, and summing up the results. This process is repeated for all rows and columns to produce the elements of the resulting matrix.

# To compute the product of two matrices x and y, you need to create a new matrix newMatrix with dimensions len(x) by len(y[0]), where len(x) is the number of rows in x and len(y[0]) is the number of columns in y.

# Then, you can use nested loops to iterate over each row in x and each column in y. For each element newMatrix[i][j] in the resulting matrix, you need to compute the dot product of row i in x and column j in y. This can be done by looping over the elements in row i and column j, multiplying corresponding elements and summing up the results.

# After computing all the elements of newMatrix, you can return it from the function or print it out to display the result.
