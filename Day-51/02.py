# Find insertion position of a target.

def insertation_position(nums , k):

    for i in range(len(nums)-1):

        if nums[i] < k < nums[i+1]:
            nums.insert(i+1 , k)

    return nums

print(insertation_position([1,2,3,5,6,7,8] , 4))