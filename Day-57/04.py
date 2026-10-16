# Reverse an array using two pointers.

def reverse_array(nums):

    left = 0
    right = len(nums) - 1

    while left <= right:

        nums[left] , nums[right] = nums[right] , nums[left]
        left += 1
        right -= 1

    return nums

print(reverse_array([1,2,3,4,5,6,7,8,9,0]))