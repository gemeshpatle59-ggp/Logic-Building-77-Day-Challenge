# Compare brute-force and sliding-window solutions for the same problem.

# Brute-Force Approach

def longest_subarray_brute(nums, k):

    max_length = 0
    n = len(nums)

    for i in range(n):
        seen = set()

        for j in range(i, n):

            seen.add(nums[j])

            if len(seen) > k:
                break

            length = j - i + 1

            if length > max_length:
                max_length = length

    return max_length


nums = [1, 2, 1, 2, 3]
k = 2

print(longest_subarray_brute(nums, k))


# Sliding-Window Approach

def longest_subarray_window(nums, k):

    left = 0
    freq = {}
    max_length = 0

    for right in range(len(nums)):

        if nums[right] in freq:
            freq[nums[right]] += 1
        else:
            freq[nums[right]] = 1

        while len(freq) > k:

            freq[nums[left]] -= 1

            if freq[nums[left]] == 0:
                del freq[nums[left]]

            left += 1

        length = right - left + 1

        if length > max_length:
            max_length = length

    return max_length


nums = [1, 2, 1, 2, 3]
k = 2

print(longest_subarray_window(nums, k))

"""
| Feature         | Brute Force               | Sliding Window     |
| --------------- | ------------------------- | ------------------ |
| Technique       | Nested loops              | Two pointers       |
| Data structure  | Set                       | Dictionary         |
| Time complexity | `O(n²)` worst case        | `O(n)`             |
| Auxiliary space | `O(K)` for `K > 0`        | `O(K)` for `K > 0` |
| Implementation  | Relatively simple         | Thodi zyada logic  |
| Large arrays    | Comparatively slow        | Comparatively fast |
| Best use        | Learning and small inputs | Efficient solution |
"""