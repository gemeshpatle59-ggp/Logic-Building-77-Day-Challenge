# Find the largest two distinct digits

num = 76438

def two_distinct(num):
    digit = [0,0]

    while num > 0:
        last_digit = num % 10
        if digit[0] < last_digit:
            # digit[1] = digit[0]
            digit[0] = last_digit

        else:
            digit[1] = last_digit    

        num = num // 10    

            

    return digit
print(two_distinct(num))        
