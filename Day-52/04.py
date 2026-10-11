# Find the number of swaps performed by bubble sort.

def bubble_sort(nums):

    num_swaped = 0

    for i in range(len(nums) -2 , -1 , -1):
        is_swaped = False
        for j in range(0 , i+1):
            if nums[j] < nums[j+1]:
                nums[j] , nums[j+1] = nums[j+1], nums[j]
                is_swaped = True
                num_swaped += 1

        if is_swaped == False:
            break


    return (f"{nums} \nnum of swaped = {num_swaped}")

print(bubble_sort([1,2,5,4,6,8,3,5]))