# Find numbers whose product of digits equals K.

def find_digit_product_k(start , end , k):

    for i in range(start , end ):
        j = i
        temp = 1
        while j > 0:
            temp *= j % 10
            j = j // 10

        if temp == k:
            print(i)


find_digit_product_k(10 , 1000 , 10)
