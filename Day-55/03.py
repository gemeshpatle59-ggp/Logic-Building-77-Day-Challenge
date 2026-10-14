# Find elements appearing in all three lists.

def find_element_in_all_list(list1 , list2 , list3):

    hash_map = {}
    elements = []

    for num in list1:
        hash_map[num] = 0

    for num in list2:
        if num in hash_map:
            hash_map[num] = 1

    for num in list3:
        if num in hash_map:
            hash_map[num] = 2


    for key in hash_map:
        if hash_map[key] == 2:
            elements.append(key)

    return elements


a = [1,4,5,2]
b = [9,2,0,1]
c = [4,1,9,2]

print(find_element_in_all_list(a,b,c))