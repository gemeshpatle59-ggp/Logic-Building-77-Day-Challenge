# Search for an element in a matrix.

def search_k_in_matrix(matrix , k):

    for row in matrix:
        for col in row:
            if col == k:
                return True

    return False

print(search_k_in_matrix([[1,  2,  3,  4],
                          [5,  6,  7,  8],
                          [9,  10, 11, 12],
                          [13, 14, 15, 16]] , 13))