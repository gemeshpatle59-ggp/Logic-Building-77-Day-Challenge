# Implement selection sort.

def seleaction_sort(nums):

    for i in range(len(nums)):
        min_idx = i

        for j in range(i+1 , len(nums)):
            if nums[j] < nums[min_idx]:
                min_idx = j

        nums[i] , nums[min_idx] = nums[min_idx] , nums[i]

    return nums

print(seleaction_sort([1,4,3,2,6,5,7,9,4]))