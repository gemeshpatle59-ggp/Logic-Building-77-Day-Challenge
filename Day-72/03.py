# Determine complexity of bubble sort.

def bubble_sort(nums):
    n = len(nums)
    for i in range(n-1):
        is_swaped = False
        for j in range(n-1-i):

            if nums[j] > nums[j+1]:
                nums[j] , nums[j+1] = nums[j+1] , nums[j]
                is_swaped = True

        if not is_swaped :
            break

    return nums

print(bubble_sort([1,2,3,4,9,8,7,6,5]))


"""
| Case | Time Complexity |
|---|---|
| Best Case (already sorted) | O(n) |
| Average Case | O(n²) |
| Worst Case (reverse sorted) | O(n²) |


"""