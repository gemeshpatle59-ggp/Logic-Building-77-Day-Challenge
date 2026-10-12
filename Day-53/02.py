# Compare best/average/worst-case behavior of basic sorting algorithms.


def bubble_sort(nums):
    count = 0

    for i in range(len(nums) - 2, -1, -1):
        is_swapped = False

        for j in range(i + 1):
            count += 1

            if nums[j] < nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                is_swapped = True

        if not is_swapped:
            break

    return count


def selection_sort(nums):
    count = 0

    for i in range(len(nums) - 1):
        max_idx = i

        for j in range(i + 1, len(nums)):
            count += 1

            if nums[j] > nums[max_idx]:
                max_idx = j

        if max_idx != i:
            nums[i], nums[max_idx] = nums[max_idx], nums[i]
            count += 1

    return count


def insertion_sort(nums):
    count = 0

    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1

        while j >= 0:
            count += 1

            if nums[j] < key:
                nums[j + 1] = nums[j]
                j -= 1
            else:
                break

        nums[j + 1] = key

    return count


nums = [1, 4, 5, 3, 6, 9, 7, 9, 4]

print("Bubble Sort:", bubble_sort(nums.copy()))
print("Selection Sort:", selection_sort(nums.copy()))
print("Insertion Sort:", insertion_sort(nums.copy()))




"""

| Algorithm               | Best Case | Average Case | Worst Case |
| ----------------------- | --------- | ------------ | ---------- |
| Bubble Sort (optimized) | O(n)      | O(n²)        | O(n²)      |
| Selection Sort          | O(n²)     | O(n²)        | O(n²)      |
| Insertion Sort          | O(n)      | O(n²)        | O(n²)      |


"""