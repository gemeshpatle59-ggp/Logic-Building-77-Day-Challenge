# Find common elements of two lists

def find_common_element_of_two_list(l1 , l2):

    hash_map = {}
    common_ele = []

    for i in l1:
        hash_map[i] = 1


    for i in l2:
        if i in hash_map:
            common_ele.append(i)

    return common_ele

print(find_common_element_of_two_list([1,2,3,5,3,5,6] , [4,3,8,7,9,6,2,1]))
