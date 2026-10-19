# Find row sums.


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def row_sum(matrix):
    for row in range(len(matrix)):
        total = 0
        for num in matrix[row]:
            total += num
        print(f"Row {row + 1} sum is {total} ")


row_sum(matrix)