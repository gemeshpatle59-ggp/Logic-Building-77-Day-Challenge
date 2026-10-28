# Given an array, find whether there exists a subarray with sum zero


def zero_sum_subarray(arr):
    n = len(arr)

    for i in range(n):
        total = 0

        for j in range(i, n):
            total += arr[j]

            if total == 0:
                return True

    return False


arr = [4, 2, -3, 1, 6]

if zero_sum_subarray(arr):
    print("Zero sum subarray exists")
else:
    print("Zero sum subarray does not exist")