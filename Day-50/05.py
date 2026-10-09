# Find the first occurrence of a target in a sorted list

def first_occurrence(nums,k):

    left = 0
    rigth = len(nums) - 1
    ans = -1

    while left <= rigth:

        mid = (left + rigth) // 2

        if nums[mid] == k:
            ans = mid
            rigth = mid - 1

        elif nums[mid] < k:
            left = mid + 1

        else:
            rigth = mid - 1

    return ans

print(first_occurrence([1,2,3,2,2,3,4,5] , 2))