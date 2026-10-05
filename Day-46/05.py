#  Rotate a list right by one position


def rotate_left(nums):

    last = nums[-1]

    for i in range( len(nums)-2,-1,-1):
        nums[i+1] = nums[i]

    nums[0] = last

    return nums


print(rotate_left([1, 2, 3, 4, 5]))