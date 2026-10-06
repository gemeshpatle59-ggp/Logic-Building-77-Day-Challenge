# 1. Rotate a list by K positions.

def rotate_element_k_place(num , k):

    n = len(num)
    k %= n
    for _ in range(k):
        key = num[n-1]
        for i in range(n-2,-1,-1):
            num[i+1] = num[i]

        num[0] = key

    return num

print(rotate_element_k_place([1,2,3,4,5] , 3))