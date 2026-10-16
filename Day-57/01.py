#  Find a pair with target sum in a sorted array using two pointers.

def targeted_sum(nums , target):

    left = 0
    right = len(nums)-1
    ans = []

    while left < right:

        if nums[left] + nums[right] == target:
            ans.append((nums[left] , nums[right]))
            left += 1
            right -= 1

        elif nums[left] + nums[right] > target:
            right -= 1

        else:
            left += 1


    return ans

print(targeted_sum([1,2,2,3,4,5] , 4))
