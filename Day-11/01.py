#  Find the first digit of a number.

num = 56776

def first_digit(num):
    n = len(str(num))

    for i in range(n):
        last_digit = num % 10
        num = num // 10

    return last_digit

print(first_digit(num))    
