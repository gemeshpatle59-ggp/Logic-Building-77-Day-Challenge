# Find all duplicate elements.

def find_all_duplicate_elements(arr):

    hash_map = {}
    duplicate = []

    for i in arr:
        if i in hash_map:
            hash_map[i] += 1

        else:
            hash_map[i] = 1

    for j in hash_map:
        if hash_map[j] > 1:
            duplicate.append(j)
        
    return duplicate

print(find_all_duplicate_elements([2,3,5,6,6,6,6,6]))
