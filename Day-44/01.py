#  Find the first repeating element.

def first_repeating_element(num):

    hash_map = {}

    for i in num:
        if i in hash_map:
            return i

        else:
            hash_map[i] = 1

    return None

print(first_repeating_element([2,4,3,5,6,2,7,8,9,9,0]))