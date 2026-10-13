# Check whether two strings are anagrams using a dictionary.

def check_anagram(l1 , l2):

    hash_map = {}

    for i in l1:
        if i in hash_map:
            hash_map[i] += 1

        else:
            hash_map[i] = 1

    for j in l2:
        if j in hash_map:
            hash_map[j] -= 1


    for key in hash_map:
        if hash_map[key] != 0:
            return False

    return True

print(check_anagram("gemesh" , "hsemeg"))