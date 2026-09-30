# Check whether a list is a palindrome.

def check_list_palindrome(nums):

    n = []

    for i in range(len(nums)-1,-1,-1):
        n.append(nums[i])

    return n == nums

print(check_list_palindrome([1,2,3,2,1]))

