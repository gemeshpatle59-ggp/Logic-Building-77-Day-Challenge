# Find the first non-repeating character.

def find_first_non_reapeating_character(chars):

    hash_map = {}

    for char in chars:
        if char in hash_map:
            hash_map[char] += 1

        else:
            hash_map[char] = 0

    for value in hash_map:

        if hash_map[value] == 0:
            return value

    else:
        return "there is no non repeating character"

print(find_first_non_reapeating_character("aabbayabyttsarstareeplkmqwplkmqwkkllz"))

        