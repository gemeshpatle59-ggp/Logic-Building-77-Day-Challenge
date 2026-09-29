# Find the sum and average of a list.


def find_sun_average(nums):

    total = 0
    average = 0


    for i in range(len(nums)):
        total += nums[i]

    average += total/len(nums)

    return (f"average = {average} , total = {total}")


print(find_sun_average([5 , 10 , 15]))