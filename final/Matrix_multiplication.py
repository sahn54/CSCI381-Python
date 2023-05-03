# MATRIX MULTIPLICATION

# Write a function matrix_mult(x,y) that takes two square “matrices” and returns their product.
def matrix_mult(m_one, m_two):
    rows = len(m_one[0])
    cols = len(m_one)
    # answer_matrix = []
    # for x in range(rows):
    #   current_row = []
    #   for y in range(cols):
    #     current_row.append(0)
    #   answer_matrix.append(current_row)
    answer_matrix = [[0 for y in range(cols)] for x in range(rows)]

    for row_number in range(rows):
        for col_number in range(cols):
            current_row = m_one[row_number]
            current_col = [m_two[x][col_number] for x in range(rows)]
            dot_product = 0
            for index_number in range(len(current_row)):
                dot_product += current_row[index_number] * \
                    current_col[index_number]
            answer_matrix[row_number][col_number] = dot_product
    return answer_matrix


square_matrix_one = [[2, 3], [4, 1]]
square_matrix_two = [[0, -2], [-1, 5]]
print(matrix_mult(square_matrix_one, square_matrix_two))

# expected answer: [[-3,11],[-1,-3]]

# row 1 column 2: row 1(2,3) column 2 (-2,5)
