# Build a frequency dictionary for a string.

def frequency_dict_str(s):

    hash_map = {}

    for i in s:
        if i in hash_map:
            hash_map[i] += 1

        else:
            hash_map[i] = 1

    for key , val in hash_map.items():
        print(f"{key} = {val}")


frequency_dict_str("gemesh patle")