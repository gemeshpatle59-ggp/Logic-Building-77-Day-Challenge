# Find the maximum frequency and all elements having that frequency.

def maximum_frequency(nums):

    freq = {}

    for i in nums:

        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    max_freq = 0

    for i in freq:
        if freq[i] > max_freq:
            max_freq = freq[i]

    result = []

    for i in freq:
        if freq[i] == max_freq:
            result.append(i)

    return max_freq, result


nums = [1, 2, 2, 3, 3, 4, 4]

print(maximum_frequency(nums))