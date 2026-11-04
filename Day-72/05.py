# Determine complexity of insertion sort

def insertion_sort(nums):
    n = len(nums)

    for i in range(1 , n):
        key = nums[i]
        j = i-1

        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1


        nums[j + 1] = key

    return nums

print(insertion_sort([5, 3, 8, 1, 2]))

"""

| Case | Time Complexity |
|---|---|
| Best Case (already sorted) | O(n) |
| Average Case | O(n²) |
| Worst Case (reverse sorted) | O(n²) |

"""
