# Check whether digits are non-decreasing or non-increasing

num = 987654

def non_increasing_or_non_decreasing_number(num):
    num = str(num)

    increasing = True
    decreasing = True

    for i in range(len(num) - 1):

        if num[i] > num[i + 1]:
            increasing = False

        if num[i] < num[i + 1]:
            decreasing = False

    if increasing:
        print("The digits are non-decreasing.")
    elif decreasing:
        print("The digits are non-increasing.")
    else:
        print("The digits are neither non-decreasing nor non-increasing.")

non_increasing_or_non_decreasing_number(num)