# Find the column with the maximum sum.

def maximum_coloum_sum(matrix):

    coloum = []
    maxm = float("-inf")

    for col in range(len(matrix[0])):
        temp = 0
        temp_col = []
        for row in range(len(matrix)):
            temp += matrix[row][col]
            temp_col.append(matrix[row][col])

        if temp > maxm:
            maxm = temp
            coloum = temp_col

    return coloum

matrix = [
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
]

print(maximum_coloum_sum(matrix))