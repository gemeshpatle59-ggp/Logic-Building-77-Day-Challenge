# Find numbers whose digit sum equals K.

def find_digit_sum_k(start , end , k):

    for i in range(start , end + 1):
        j = i
        temp = 0
        while j > 0:
            temp += j % 10
            j = j // 10

        if temp == k:
            print(i)

find_digit_sum_k(10 , 1000 , 8)

            