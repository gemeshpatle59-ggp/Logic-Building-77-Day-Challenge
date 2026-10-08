# Return the first index of a target.


def first_idx(nums , k):

    for i in range(len(nums)):

        if nums[i] == k:
            return i

    return -1

print(first_idx( [5, 2, 7, 2, 9, 2] , 2))