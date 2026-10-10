#  Find the last occurrence of a target in a sorted list.

def last_occurrence(nums , k):

    idx = 0

    for i in range(len(nums)):
        if nums[i] == k:
            idx = i


    return idx

print(last_occurrence([1,2,3,4,2,3,6,2] , 2))

