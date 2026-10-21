# Check whether a matrix is symmetric.

def matrix_symmetric(matrix):

    transpose = []

    for col in range(len(matrix[0])):
        temp = []
        for row in range(len(matrix)):
            temp.append(matrix[row][col])

        transpose.append(temp)


    return transpose == matrix

print(matrix_symmetric([
                            [1, 2, 3],
                            [2, 4, 5],
                            [3, 5, 6]
                                        ]))
