# Find elements present in one list but not the other.


def find_ele(l1 , l2):

    hash_map = {}
    new_ele = []


    for i in l1:
        hash_map[i] = 1

    for j in l2:
        if j not in hash_map:
            new_ele.append(j)


    return new_ele

print(find_ele([1,2,3,4] , [1,2,5,6]))