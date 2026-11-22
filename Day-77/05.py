# Find the minimum frequency and all elements having that frequency

def minimum_frequency(nums):

    freq = {}

    for i in nums:

        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    min_freq = len(nums)

    for i in freq:
        if freq[i] < min_freq:
            min_freq = freq[i]

    result = []

    for i in freq:
        if freq[i] == min_freq:
            result.append(i)

    return min_freq, result


nums = [1, 2, 2, 3, 3, 4, 4]

print(minimum_frequency(nums))