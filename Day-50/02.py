# Implement binary search on a sorted list.

def binary_search(nums , k):

    left = 0
    right = len(nums)-1

    while left <= right:

        mid = (left + right) // 2

        if nums[mid] == k:
            return mid

        elif nums[mid] > k:
            right = mid - 1

        else:
            left = mid + 1

    return -1

print(binary_search([1,3,2,2,4,5,3,4] , 5))
        

