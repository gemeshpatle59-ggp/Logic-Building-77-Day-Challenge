# Check whether a number is an automorphic number

num = 25

def automorphic(num):
    n = num ** 2
    m = len(str(num))
    if num >= 0 and n % (10**m) == num:
        print(f"{num} is a automorphic number..")
    else:
        print(f"{num} is not a automorphic number..")    

automorphic(num)