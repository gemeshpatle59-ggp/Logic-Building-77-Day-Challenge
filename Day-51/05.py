# Implement insertion sort

def insertion_sort(nums):

    for i in range(1 , len(nums)):

        key = nums[i]
        j = i-1

        while j >= 0 and nums[j] > key:
            nums[j+1] = nums[j]
            j -= 1

        nums[j+1] = key

    return nums

print(insertion_sort([1,5,4,2,7,9,5,6]))