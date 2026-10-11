# Sort numbers by frequency.

def sort_by_frwequency(nums):

    hash_map = {}
    high = 0

    for i in nums:
        if i in hash_map:
            hash_map[i] += 1

            if hash_map[i] > high:
                high = hash_map[i]

        else:
            hash_map[i] = 1

    nums.sort(key=lambda x: (-hash_map[x] , x))

    print(nums)

    
sort_by_frwequency([4,4,1,2,2,2,3])