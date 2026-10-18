# Find the longest subarray with at most K distinct values.

def longest_subarray(nums, k):

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

print(longest_subarray(nums, k))