# Implement bubble sort.

def bubble_sort(nums):

    for i in range(len(nums)-1):
        if_isawaped = False

        for j in range(len(nums)-1-i):
            if nums[j] > nums[j+1]:
                nums[j] , nums[j+1] = nums[j+1] , nums[j]
                if_isawaped = True

        if if_isawaped == False:
            break

    return nums

print(bubble_sort([1,6,4,2,8,5,2]))