#  Move all zeros to the end while preserving the order of other elements.

# def move_zeros_end(nums):

#     for j in range(len(nums)-1):
#         for i in range(j+1,len(nums)):

#             if nums[i-1] == 0:
#                 nums[i] , nums[i-1] = nums[i-1], nums[i]


#     return nums


# print(move_zeros_end([1,3,0,4,0,8,0,5,0]))



def move_zeros_end(nums):
    j = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j], nums[i] = nums[i], nums[j]
            j += 1

    return nums


print(move_zeros_end([1,3,0,4,0,8,0,5,0]))