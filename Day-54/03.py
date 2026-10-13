# Find the first non-repeating character using a frequency dictionary.

def firstNonrepeating(nums):

    freq_map = {}

    for i in nums:
        if i in freq_map:
            freq_map[i] += 1

        else:
            freq_map[i] = 1

    for i in freq_map:
        if freq_map[i] == 1:
            return i

    return None

print(firstNonrepeating([1,2,3,1,4,5,6,5,4,7,8,9,8,9]))