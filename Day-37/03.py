# Check whether two strings are anagrams.

def check_anagrams(s1 , s2):

    hash_map = {}

    if len(s1) != len(s2):
        return False

    hash_map = {}

    for i in s1:
        if i in hash_map:
            hash_map[i] += 1

        else:
            hash_map[i] = 1

    for j in s2:
        if j in hash_map:
            hash_map[j] -= 1

    for key , value in hash_map.items():
        if value != 0:
            return False

    return True

print(check_anagrams("banana" , "ananab"))