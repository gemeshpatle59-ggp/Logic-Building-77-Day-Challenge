# Find the sum of a list recursively.

def sum(nums,n):
    if n == 0:
        return nums[0]

    return sum(nums , n-1) + nums[n-1]

print(sum([1,2,3] , 3))