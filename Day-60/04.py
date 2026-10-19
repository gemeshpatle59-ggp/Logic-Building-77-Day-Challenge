# Find the largest element in a matrix.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def largest_element(matrix):

    largest = float("-inf")

    for row in matrix:
        for num in row:
            if num > largest:
                largest = num

    return largest

print(largest_element(matrix))
