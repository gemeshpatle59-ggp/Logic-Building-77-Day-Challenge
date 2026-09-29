# Count positive, negative, and zero elements

def count_pos_neg_zero(nums):

    positive = 0
    negative = 0
    zero = 0


    for i in nums:
        if i == 0:
            zero += 1

        elif i < 0:
            negative += 1

        else:
            positive += 1

    return(f"positive element are = {positive}\nnegative element are is {negative}\nzeros are = {zero}")

print(count_pos_neg_zero([1,3,4,0,0,0,4,5,7,4,7,8,8,6,-9,-4,-8,-8]))