# Remove duplicate characters while preserving order.


def remove_duplicate(s):
    hash_map = {}
    new_str = ""
    for i in s:
        if i not in hash_map:
            hash_map[i] = 0

    for i in hash_map:
        new_str += i

    return new_str

print(remove_duplicate("banana"))

