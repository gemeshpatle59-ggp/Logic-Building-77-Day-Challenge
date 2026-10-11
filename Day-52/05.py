# Compare linear search and binary search on sorted data

def linear_search(nums , k):

    count = 0

    for i in range(len(nums)):
        count += 1

        if nums[i] == k:
            return("found at index", i,"at count =",count)

        

def binary_search(nums , k):

    count = 0
    left = 0
    right = len(nums) -1

    while left <= right:

        count += 1
        mid = (left + right) // 2

        if nums[mid]  == k:
            return ("found at index", mid,"at count = ",count)

        elif nums[mid] < k:
            left = mid + 1

        else:
            right = mid - 1


nums = [1,2,3,4,5,6,7]
k = 7

print(linear_search(nums , k))
print(binary_search(nums , k))

        

