# Print the main diagonal.

def print_main_diagonal(matrix):

    diagonal = []

    for row in range(min(len(matrix) , len(matrix[0]))):
        for col in range(row , row+1):
            diagonal.append(matrix[row][col])

    return diagonal

print(print_main_diagonal([[1,2,3],
                           [3,4,5]]))

