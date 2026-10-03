# 1. Find union of two lists.

def union_of_two_list(l1, l2):

    new_list = []
    hash_map = {}

    for i in l1:
        hash_map[i] = 1

    for j in l2:
        hash_map[j] = 1

    for k in hash_map:
        new_list.append(k)

    return new_list


print(union_of_two_list(
    [1,2,3,4,32,4],
    [4,5,6,2,3,4,34]
))