# Find the maximum sum of two elements.


def find_maxm_sum_0f_two_element(nums):

    maxm_sum = nums[0]
    maxm = 0

    for i in range(1 , len(nums)):
        if nums[i] > maxm_sum:
            maxm = maxm_sum
            maxm_sum = nums[i]

        else:
            if nums[i] > maxm:
                maxm = nums[i]


    return maxm + maxm_sum


print(find_maxm_sum_0f_two_element([3,8,1,6,5]))
