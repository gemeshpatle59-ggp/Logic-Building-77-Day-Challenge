# Transpose a matrix.

def transpose_0f_matrix(matrix):

    transpose_matrix = []

    for col in range(len(matrix[0])):
        temp = []
        for row in range(len(matrix)):
            temp.append(matrix[row][col])

        transpose_matrix.append(temp)
        
    return transpose_matrix

print(transpose_0f_matrix([[1,2,3],[4,5,6]]))
