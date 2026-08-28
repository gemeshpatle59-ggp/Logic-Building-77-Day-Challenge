#  Find the sum of digits.

num = -453

def total_digit(num):
    num = abs(num)

    total = 0
    while num > 0:
        last_digit = num % 10
        total += last_digit
        num = num // 10
        
    return total

print(total_digit(num))    
