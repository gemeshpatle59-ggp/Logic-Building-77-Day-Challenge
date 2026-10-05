# Move all negative numbers to one side.

def move_negative_one_side(nums):

    j = 0

    for i in range(len(nums)):

        if nums[i] > 0 :
            nums[i] , nums[j] = nums[j] , nums[i]
            j += 1

    return nums


print(move_negative_one_side([1,4,6,3,9,-7,5,-2,-4,7,8,5,4]))