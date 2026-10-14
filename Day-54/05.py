# Find pairs with a target sum using hashing

def find_pair_sum(nums , target):

    seen = set()
    pair = []

    for num in nums:

        complement = target - num

        if complement in seen:
            pair.append((complement , num))

        seen.add(num)

    return pair

print(find_pair_sum([2, 7, 4, 5, 3, 6] , 9))