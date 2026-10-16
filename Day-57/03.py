# Move zeros to the end using two pointers.

def move_zerostoEnd(nums):

    for i in range(len(nums)):
        if nums[i] == 0:
            j = i
            while j < len(nums):
                if nums[j] != 0:
                    nums[i] , nums[j] = nums[j] , nums[i]
                j += 1

    return nums

print(move_zerostoEnd([1,2,3,0,0,4,0,0,0,0,0,0,4,5,3,2,0]))
