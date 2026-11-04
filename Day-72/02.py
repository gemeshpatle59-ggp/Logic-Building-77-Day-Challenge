# Determine complexity of binary search.

def binary_search(n , k):

    i = 0
    j = len(n)-1

    while i <= j:
        mid = (i + j)//2

        if n[mid] == k:
            print("Element found at index", mid)
            break

        elif n[mid] < k:
            i = mid + 1

        else:
            j = mid - 1

    else:
        print("not found")

"""
| Case | Time Complexity |
|---|---|
| Best Case | O(1) |
| Average Case | O(log n) |
| Worst Case | O(log n) |

"""