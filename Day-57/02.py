# Remove duplicates from a sorted array in-place.

def remove_duplicate_in_sorted_array(nums):

    i = 0

    for j in range(1 , len(nums)):

        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]

    return nums[:i + 1]

print(remove_duplicate_in_sorted_array([1,1,1,2,2,2,3,3,3,4,4,4,5,5,5]))
