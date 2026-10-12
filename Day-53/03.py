# Build a frequency dictionary for a list.

def frequency_dict(nums):

    hash_map = {}

    for i in nums:
        if i in hash_map:
            hash_map[i] += 1

        else:
            hash_map[i] = 1

    return hash_map

print(frequency_dict([1,2,2,2,3,4,5,6,5,5,4,3,4,5]))