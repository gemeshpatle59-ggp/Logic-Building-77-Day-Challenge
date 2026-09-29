# Find maximum and minimum in a list without max/min.

def find_min_max(nums):

    maxm = 0
    minm = float("inf")

    for i in nums:
        if i > maxm:
            maxm = i

        if i < minm:
            minm =  i


    return (f"maxm in list is '{maxm}' and minimun is '{minm}'")


nums = [2,5,3,6,8,2,8]

print(find_min_max(nums))
        








