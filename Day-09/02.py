# Extract and print every digit of a number.

num = -453

def count_digit(num):
    num = abs(num)

    while num > 0:
        last_digit = num % 10
        print(last_digit)
        num = num // 10

(count_digit(num))    
