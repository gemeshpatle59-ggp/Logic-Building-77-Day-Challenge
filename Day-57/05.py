#  Check palindrome using two pointers

def check_palindrome(nums):

    left = 0
    right = len(nums) - 1

    while left < right:
        if nums[left] != nums[right]:
            return False

        left += 1
        right -= 1

    return True

print(check_palindrome([1,2,3,3,2,1]))