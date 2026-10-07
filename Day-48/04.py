# Find the maximum subarray sum by brute force first, then improve it.

def find_maximum_subarray_sum(nums):

    maxm = 0

    for i in range(len(nums)):
        temp = 0
        j = len(nums) - 1

        while i < j:
            if temp > maxm:
                maxm = temp

            temp += nums[j]
            j -= 1


    return maxm

print(find_maximum_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
            
