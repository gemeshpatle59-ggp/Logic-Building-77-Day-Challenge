# Implement binary search iteratively.

def binary_search(nums , k):

    left = 0
    right = len(nums) - 1

    while left <= right:

        mid = (left + right) // 2

        if nums[mid] == k:
            return mid

        elif nums[mid] < k:
            left = mid + 1

        else:
            right = mid - 1

    return -1

print(binary_search([1,2,3,4,5,6,7,8,9] , 2))