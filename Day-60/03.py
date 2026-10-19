# Find column sums.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def column_sum(matrix):

    for col in range(len(matrix[0])):
        total = 0
        for num in range(len(matrix)):
            total += matrix[num][col]

        print(f"Col {col + 1} sum is {total}")

column_sum(matrix)