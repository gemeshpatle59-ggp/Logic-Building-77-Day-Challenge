# Find the maximum difference between two elements with the larger element appearing later.


def maxm_difference_between_two_elements(nums):

    min_ele = nums[0]
    maxm_diff = float("-inf")

    for i in range(1 , len(nums)):

        if nums[i] - min_ele > maxm_diff:
            maxm_diff = nums[i] - min_ele

        if nums[i] < min_ele:
            min_ele = nums[i]
        

    return maxm_diff

print(maxm_difference_between_two_elements([2,5,1,8,3]))