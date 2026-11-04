# Determine complexity of selection sort.


def selection_sort(nums):
    n = len(nums)

    for i in range(n-1):
        min_idx = i

        for j in range(i+1 , n):
            if nums[j] < nums[min_idx]:
                min_idx = j

        nums[i] , nums[min_idx] = nums[min_idx] , nums[i]

    return nums

print(selection_sort([64, 25, 12, 22, 11]))


"""
| Case | Time Complexity |
|---|---|
| Best Case | O(n²) |
| Average Case | O(n²) |
| Worst Case | O(n²) |

"""