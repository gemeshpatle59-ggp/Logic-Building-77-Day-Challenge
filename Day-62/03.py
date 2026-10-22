# Print the secondary diagonal.

def secondary_diagonal(matrix):

    diagonal = []
    j = -1

    for row in range(min(len(matrix) , len(matrix[0]))):
        
        diagonal.append(matrix[row][j])
        j -= 1

    return diagonal

print(secondary_diagonal([[1,2],
                         [4,5],
                         [7,8]]))