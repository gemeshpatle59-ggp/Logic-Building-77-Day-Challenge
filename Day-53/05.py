# Find duplicates using a set

def find_duplicate_using_set(nums):

    hash_set = set()
    duplicate = []

    for i in nums:
        if i in hash_set:
            duplicate.append(i)

        hash_set.add(i)

    return duplicate

print(find_duplicate_using_set([1,2,3,4,2,3,4,5]))

