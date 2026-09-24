# Find the first repeating character.

def find_the_first_repeating_character(chars):

    hash_map = {}

    for char in chars:

        if char in hash_map:
            hash_map[char] += 1
            return char

        else:
            hash_map[char] = 0

    else:
        return "no repeating character "

print(find_the_first_repeating_character("asdfghhjkuyaabfgduu"))