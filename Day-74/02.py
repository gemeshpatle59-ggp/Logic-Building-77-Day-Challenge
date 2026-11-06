"""
Build an array analyzer that reports min/max, second largest, duplicates, frequency, sorted status, missing
value, and pair-sum results.

"""


arr = [1, 3, 5, 3, 7, 9, 1, 2]

print("Original Array:", arr)

# 1. Minimum and Maximum
print("Minimum:", min(arr))
print("Maximum:", max(arr))

# 2. Second Largest
unique = list(set(arr))
unique.sort()

if len(unique) >= 2:
    print("Second Largest:", unique[-2])
else:
    print("Second Largest does not exist")

# 3. Duplicate Elements
duplicates = []

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] == arr[j] and arr[i] not in duplicates:
            duplicates.append(arr[i])

print("Duplicates:", duplicates)

# 4. Frequency of Each Element
freq = {}

for i in arr:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print("Frequency:", freq)

# 5. Check Sorted Status
ascending = True

for i in range(len(arr) - 1):
    if arr[i] > arr[i + 1]:
        ascending = False
        break

if ascending:
    print("Array is Sorted")
else:
    print("Array is Not Sorted")

# 6. Find Missing Value
n = 9
expected_sum = n * (n + 1) // 2
actual_sum = sum(set(arr))

print("Missing Value (if applicable):", expected_sum - actual_sum)

# 7. Pair Sum
target = 10
pairs = []

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == target:
            pairs.append((arr[i], arr[j]))

print("Pairs with Sum", target, ":", pairs)
