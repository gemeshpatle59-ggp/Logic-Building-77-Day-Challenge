# Add two matrices.

def add_two_matrix(matrix1 , matrix2):

    new_matrix = []

    for row in range(len(matrix1)):
        temp = []
        for col in range(len(matrix1[row])):
            temp.append(matrix1[row][col] + matrix2[row][col])

        new_matrix.append(temp)

    return new_matrix

print(add_two_matrix([[1,2],
                      [3,4]],   [[5,6],
                                 [7,8]]))
