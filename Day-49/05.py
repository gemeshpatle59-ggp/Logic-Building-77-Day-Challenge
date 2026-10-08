# Return all indices of a target


def first_idx(nums , k):

    idx = []

    for i in range(len(nums)):

        if nums[i] == k:
            idx.append(i)

    return idx

print(first_idx( [5, 2, 7, 2, 9, 2] , 2))