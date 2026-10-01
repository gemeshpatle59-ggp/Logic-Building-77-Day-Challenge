# Count frequency of every element.

def count_frequency_of_every_element(arr):

    hash_map = {}

    for i in arr:
        if i in hash_map:
            hash_map[i] += 1

        else:
            hash_map[i] = 1

    return hash_map

print(count_frequency_of_every_element([2,3,5,6,6,6,6,6]))