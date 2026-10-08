# Implement linear search.

def linear_search(nums , k):

    for i in range(len(nums)):
        if nums[i] == k:
            return i

    return -1

print(linear_search([10,25,7,18,30] , 18))