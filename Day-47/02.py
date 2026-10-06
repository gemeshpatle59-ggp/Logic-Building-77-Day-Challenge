# Find the missing number from 1 to N.

def find_missing_num_1_n(nums , n):

    missing = []
    hash_map = {}

    for i in nums:
        hash_map[i] = 1

    for j in range(1,n+1):
        if j not in hash_map:
            missing.append(j)


    return missing

print(find_missing_num_1_n([1,5,3,8] , 10))