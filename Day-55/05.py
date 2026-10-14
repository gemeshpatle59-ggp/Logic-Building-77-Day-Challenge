# Find the element with maximum frequency

def find_element_with_maxm_frequency(nums):

    freq = 0
    hash_map = {}

    for num in nums:

        if num in hash_map:
            hash_map[num] += 1

        else:
            hash_map[num] = 1

        if hash_map[num] > freq:
            freq = num

    return freq

print(find_element_with_maxm_frequency([1,2,3,4,5,2,6,5,2,2,2,8,2,7,3,8,9]))        