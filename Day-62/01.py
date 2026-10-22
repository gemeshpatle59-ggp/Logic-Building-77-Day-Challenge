#  Multiply two matrices using nested loops.

def multiply_matrices(A, B):

    rows_A = len(A)
    cols_A = len(A[0])
    cols_B = len(B[0])

    result = []

    for i in range(rows_A):
        row = []

        for j in range(cols_B):
            total = 0

            for k in range(cols_A):
                total += A[i][k] * B[k][j]

            row.append(total)

        result.append(row)

    return result


A = [[1, 2],[3, 4]]

B = [[5, 6],
     [7, 8]]

print(multiply_matrices(A, B))