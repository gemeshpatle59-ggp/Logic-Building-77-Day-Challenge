#  Print a matrix in spiral order.

def spiral_ordar_matrix(matrix):

    top = 0
    bottom = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1


    while top <= bottom and left <= right:

        for i in range(left , right+1):
            print(matrix[top][i] , end=" ")

        top += 1

        for i in range(right , bottom+1):
            print(matrix[i][right] , end=" ")

        right -= 1

        if top <= bottom:
            for i in range(right , left-1 , -1):
                print(matrix[bottom][i] , end=" ")
            bottom -= 1

        if left <= right:
            for i in range(bottom , top-1 , -1):
                print(matrix[i][left] , end=" ")

            left += 1

spiral_ordar_matrix([[1,  2,  3,  4],
                     [5,  6,  7,  8],
                     [9,  10, 11, 12],
                     [13, 14, 15, 16]])



        

            