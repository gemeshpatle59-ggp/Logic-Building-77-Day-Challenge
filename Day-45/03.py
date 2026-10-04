# Merge two sorted lists.

def merge_two_sorted_list(l1 , l2):

    hash_map = {}
    merge_list = []

    i = 0
    j = 0

    while i < len(l1) and j < len(l2):

        if l1[i] < l2[j]:
            merge_list.append(l1[i])
            i += 1

        else:
            merge_list.append(l2[j])
            j += 1

    while i < len(l1):
        merge_list.append(i)
        i += 1


    while j < len(l2):
        merge_list.append(l2[j])
        j += 1

    return merge_list

print(merge_two_sorted_list([1,2,3,6,7] ,[4,5,8,9]))
        