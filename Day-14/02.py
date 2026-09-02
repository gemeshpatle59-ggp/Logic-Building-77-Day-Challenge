# Check whether digits are strictly increasing from left to right

num = 1235678

def increasing_digit(num):
    num = str(num)
    first_digit = -1

    for i in num:
        if int(i) > first_digit:
            first_digit = int(i)

        else:
            print("The digits are not strictly incresing for left to right..")
            return

    print("The digits are strictly incresing for left to right.")    

increasing_digit(num)            
