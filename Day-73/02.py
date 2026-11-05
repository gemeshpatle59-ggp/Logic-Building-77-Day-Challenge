# Compare brute-force pair-sum with hashing pair-sum.

"""
| Feature | Brute-Force Approach | Hashing Approach |
|---|---|---|
| Method | Checks every possible pair | Uses a set to find the required complement |
| Nested loops | Yes | No |
| Time Complexity | O(n²) | O(n) average |
| Space Complexity | O(1) | O(n) |
| Main advantage | Simple to understand and implement | Faster for large arrays |
| Main disadvantage | Slow for large arrays | Requires extra memory |

"""

# BRUTE FORCE

arr = [2, 7, 11, 15]
target = 9

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == target:
            print(arr[i], arr[j])


# HASHING APPROCH

arr = [2, 7, 11, 15]
target = 9

seen = set()

for x in arr:
    complement = target - x

    if complement in seen:
        print(complement, x)
        break

    seen.add(x)