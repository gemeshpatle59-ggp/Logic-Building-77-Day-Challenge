# Given an array, find the longest strictly increasing contiguous subarray.

def longest_increasing_subarray(array):

    longest_arr = []
    longest = 0
    temp = 0
    temp1 = []

    for i in range(len(array) - 1):
        if array[i] < array[i + 1]:
            if temp == 0:
                temp1 = [array[i]]

            temp += 1
            temp1.append(array[i + 1])

        else:
            if temp > longest:
                longest = temp
                longest_arr = temp1.copy()

            temp1 = []
            temp = 0

    if temp > longest:
        longest_arr = temp1.copy()

    return longest_arr

array = [34, 55, 1, 2, 3, 4, 5, 21, 22, 23]

print(longest_increasing_subarray(array))

