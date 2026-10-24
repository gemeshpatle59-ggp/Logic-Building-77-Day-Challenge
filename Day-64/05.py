# Find all Armstrong numbers in a range without converting numbers to strings

def find_armstrong(start , end):

    for i in range(start , end):
        j = i
        len = 0
        while j > 0:
            len += 1
            j = j // 10

        l = i
        arm = 0
        while l > 0:
            last_digit = l % 10
            arm += last_digit**len
            l = l // 10

        if i == arm:
            print(i)


find_armstrong(10 , 200)