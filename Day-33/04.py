# Count occurrences of a value in a list recursively.

def count_occurrence(arr, n, target):
    if n == 0:
        return 0

    if arr[n - 1] == target:
        return 1 + count_occurrence(arr, n - 1, target)
    else:
        return count_occurrence(arr, n - 1, target)


arr = [2, 5, 2, 7, 2, 8, 5]

print(count_occurrence(arr, len(arr), 2))