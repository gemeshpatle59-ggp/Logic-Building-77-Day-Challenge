# Find all unique elements.

def find_all_unique_elements(arr):

    hash_map = {}
    unique = []

    for i in arr:
        if i in hash_map:
            hash_map[i] += 1

        else:
            hash_map[i] = 1

    for j in hash_map:
        if hash_map[j] == 1:
            unique.append(j)
        
    return unique

print(find_all_unique_elements([2,3,5,6,6,6,6,6]))
