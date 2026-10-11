# Sort a list of strings by length.

def sort_string_in_list_by_length(l1):

    hash_map = {}

    for i in l1:

        hash_map[i] = len(i)


    l1.sort(key = lambda x : (hash_map[x] , x))

    return l1

print(sort_string_in_list_by_length(["apple", "hi", "banana", "cat", "dog"]))