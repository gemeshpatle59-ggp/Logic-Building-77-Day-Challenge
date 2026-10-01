# Find the most frequent element.

def count_most_frequency_element(arr):

    hash_map = {}
    most = 0
    ele = ""
    for i in arr:
        if i in hash_map:
            hash_map[i] += 1

        else:
            hash_map[i] = 1

    for j in hash_map:
        if hash_map[j] > most:
            most = hash_map[j]
            ele = j


    return ele

print(count_most_frequency_element([2,3,5,6,6,6,6,6]))