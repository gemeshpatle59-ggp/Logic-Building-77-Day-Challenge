# Determine complexity of linear search.


def linear_search(n , k):


    for i in n:
        if i == k:
            return True
    return False

n = int(input("list of nums"))
k = int(input("element to find"))

"""

| Case | Number of Comparisons | Time Complexity |
|---|---|---|
| Best Case | 1 | O(1) |
| Average Case | n/2 | O(n) |
| Worst Case | n | O(n) |

"""

