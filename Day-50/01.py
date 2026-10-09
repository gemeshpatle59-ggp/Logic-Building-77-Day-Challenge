#  Count occurrences of a target using search.

def count_accurremces_of_target(nums , k):

    count = 0

    for i in nums:
        if i == k:
            count += 1

    return count

print(count_accurremces_of_target([1,2,2,3,4,2,5,6,3] , 2))
