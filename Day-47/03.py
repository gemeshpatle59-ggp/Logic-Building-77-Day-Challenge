# Find a duplicate number when one value repeats.

def find_repeat_value(nums):

    hash_map = {}
    ans_ele = []

    for i in nums:
        if i in hash_map:
            hash_map[i] += 1

        else:
            hash_map[i] = 1

    for j in hash_map:
        if hash_map[j] > 1:
            ans_ele.append(j)

    return ans_ele

print(find_repeat_value([1,1,3,4,5,6,3,3,2,2,2,7,6,7,7,9]))
