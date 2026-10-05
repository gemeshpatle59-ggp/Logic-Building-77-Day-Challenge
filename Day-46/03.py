# Separate even and odd elements.

def seperate_even_odd(nums):

    j = 0

    for i in range(len(nums)):

        if nums[i] % 2 == 0:
            nums[i] , nums[j] = nums[j] , nums[i]

            j += 1

    return nums

print(seperate_even_odd([2,3,4,5,6,7,8]))

