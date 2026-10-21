#  Count zeros, positive, and negative elements.

def count_zeros_negative_positive(matrix):

    negative = 0
    positive = 0
    zeros = 0

    for row in matrix:
        for num in row:
            if num < 0:
                negative += 1

            elif num > 0:
                positive += 1

            else:
                zeros += 1


    return (f"negative = {negative}\n"
            f"positive = {positive}\n"
            f"zeros    = {zeros}")
print(count_zeros_negative_positive([[ 1, 2, 3],
                                    [-9,-7,-6],
                                    [ 0, 0, 4]]))