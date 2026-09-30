#  Reverse a list without reverse() or slicing.

def reversse_list(nums):

    n = len(nums)
    i = 0
    j = n - 1

    while i<=j:

        nums[i] , nums[j] = nums[j] , nums[i]

        i += 1
        j -= 1

    return nums

print(reversse_list([1,2,3,4,5]))