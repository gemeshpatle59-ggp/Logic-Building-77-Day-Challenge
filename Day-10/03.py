# Find the sum of digits.

num = 4567

def add_digit(num):
    num = abs(num)

    total = 0
    while num > 0:
        last_digit = num % 10
        total += last_digit
        num = num // 10

    return total    

print(add_digit(num))