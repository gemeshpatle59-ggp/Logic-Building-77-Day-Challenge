#  Find the prefix sums of an array.

def prefix_sum(nums):

    prefix = []
    total = 0

    for i in nums:
        total += i
        prefix.append(total)

    return prefix

print(prefix_sum([2,4,3,5]))