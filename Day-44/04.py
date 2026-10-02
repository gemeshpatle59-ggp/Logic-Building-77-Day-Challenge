# Check whether two lists contain the same elements regardless of order.

def check_two_list_element_are_same(l1 , l2):

    if len(l1) != len(l2):
        return False

    hash_map = {}

    for i in l1:
        if i in hash_map:
            hash_map[i] += 1

        else:
            hash_map[i] = 1

    new_l2 = l2

    for i in range(len(new_l2)):

        if l2[i] in hash_map:
            if hash_map[l2[i]] > 0:
                hash_map[l2[i]] -= 1
                l2[i] = 0

            else:
                return False

        else:
            return False

    f = 0

    for k in l2:
        if k == 0:
           f += 1

    return f == len(l2)


print(check_two_list_element_are_same([1,2,3] , [1,2,2]))