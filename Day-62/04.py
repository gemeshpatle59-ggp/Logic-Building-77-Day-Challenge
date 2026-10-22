# Find diagonal sums.

def diagonal_sum(matrix):

    diagonal = 0

    for row in range(min(len(matrix) , len(matrix[0]))):
        for col in range(row , row+1):
            diagonal += (matrix[row][col])

    return diagonal

print(diagonal_sum([[1,2,3],
                           [3,4,5]]))

