# 1. Remove duplicates while preserving order.

def remove_duplicate(arr):

    hash_map = {}
    
    for i in range(len(arr)-1,-1,-1):
        if arr[i] in hash_map:
            del arr[i]
                
        else:
            hash_map[arr[i]] = 1


    return arr

print(remove_duplicate([2,4,5,7,5,5,4,2,2,8,9,3,9]))