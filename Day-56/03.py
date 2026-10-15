# Find the longest consecutive sequence using a set.

def longest_consecutive_sequence(nums):

    seen = set(nums)
    longest = 0

    for num in nums:
        if num-1 not in seen:
            count = 1
            current = num

            while current + 1 in seen:
                current += 1
                count += 1

            if count > longest:
                longest = count

    return longest


nums = [100, 4, 200, 1, 3, 2]
print(longest_consecutive_sequence(nums))