#  Sort a list without using sort() or sorted().

def quick_sort(nums):

    if len(nums) <= 1:
        return nums

    pivot = nums[-1]

    left = []
    right = []

    for i in range(len(nums)-1):

        if nums[i] < pivot:
            left.append(nums[i])

        else:
            right.append(nums[i])

    return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort([1,2,4,5,7,3,9,8,5,4,3]))