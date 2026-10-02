# Find the first non-repeating element.

def first_non_repeating_element(num):

    hash_map = {}
    
    for i in num:
        if i in hash_map:
            hash_map[i] += 1

        else:
            hash_map[i] = 0


    for j in hash_map:
        if hash_map[j] == 0:
            return j

    return None

print(first_non_repeating_element([2,2,3,6,4,4,7,8,9,4]))

