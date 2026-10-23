# Find the row with the maximum sum.

def maximum_sum_row(matrix):

    rows = []
    maxm = float("-inf")

    for row in matrix:
        temp = 0
        for num in row:
            temp += num

        if temp > maxm:
            maxm = temp
            rows = row


    return rows

print(maximum_sum_row([[1,2,3],
                       [4,5,6],
                       [7,8,9]]))
