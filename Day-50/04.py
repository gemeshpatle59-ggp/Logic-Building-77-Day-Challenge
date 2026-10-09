# Implement binary search recursively.

def binary_search(nums , k , left , right):

    if left > right:
        return -1

    mid = (left + right)// 2

    if nums[mid] == k:
        return mid

    elif nums[mid] < k:
        return binary_search(nums , k ,mid+1, right)

    else:
        return binary_search(nums , k , left , mid - 1)

nums = [1,2,3,4,5,6,7,8,9]

print(binary_search(nums,  5 , 0 ,len(nums) - 1))

