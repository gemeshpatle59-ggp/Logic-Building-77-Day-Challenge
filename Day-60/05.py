# Find the position of the largest element

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def find_position_largest_element(matrix):

    largest_position = []
    largest = float("-inf")

    for row in range(len(matrix)):
        for num in range(len(matrix[row])):
            if matrix[row][num] > largest:
                largest = matrix[row][num]
                largest_position = [row , num]

    return largest_position

print(find_position_largest_element(matrix))