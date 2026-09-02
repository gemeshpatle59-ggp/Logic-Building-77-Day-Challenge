#  Check whether digits are strictly decreasing from left to right


num = 987654

def decreasing_number(num):
    num = str(num)
    first_digit = float("inf")

    for i in num:
        if int(i) < first_digit:
            first_digit = int(i)

        else:
            print("The digits are not strictly decreasing for left to right..")
            return

    print("The digits are strictly decreasing for left to right.")    

decreasing_number(num)            
