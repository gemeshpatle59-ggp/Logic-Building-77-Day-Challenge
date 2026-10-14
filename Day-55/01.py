#  Count pairs whose sum equals K.

def count_pair_sum(nums , k):

    pairs_count = 0
    seen = set()

    for num in nums:

        compliment = k - num

        if compliment in seen:
            pairs_count += 1

        seen.add(num)

    return pairs_count

print(count_pair_sum([2,7,4,6,3,5] , 9))