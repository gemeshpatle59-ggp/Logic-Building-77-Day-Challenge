# 1. Find the least frequent character.

def least_frequent(s):

    has_map = {}

    for i in s:
        if i in has_map:
            has_map[i] += 1

        else:
            has_map[i] = 1

    least = float("inf")

    least_char = ""

    for key,val in has_map.items():
        if val < least:
            least = val
            least_char = key

    return least_char

print(least_frequent("aaabbeddf"))