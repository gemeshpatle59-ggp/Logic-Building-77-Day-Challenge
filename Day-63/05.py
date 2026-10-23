# Find the longest number with digits in increasing order within a range


def longest_number_with_digits(start , end):



    for i in range(end , start-1 , -1):

        n = i
        m = float("inf")
        increasing_odr = False
    
        while n > 0:
            last_digit = n % 10
            if last_digit >= m :
                increasing_odr = False
                break
            increasing_odr = True
            m = last_digit
            n = n // 10

        if increasing_odr:
            return i

    

print(longest_number_with_digits(10 , 200))


