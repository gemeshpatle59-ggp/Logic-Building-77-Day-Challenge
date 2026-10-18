#  Print all elements column by column-

def print_column_wise(matrix):

    rows = len(matrix)
    cols = len(matrix[0])

    for j in range(cols):
        for i in range(rows):
            print(matrix[i][j], end=" ")
        print()


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_column_wise(matrix)