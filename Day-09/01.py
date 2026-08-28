# Count the number of digits in an integer

num = -453

def count_digit(num):
    num = abs(num)
    if num == 0:
        return 1
    count = 0
    while num > 0:
        # last_digit = num % 10
        count += 1
        num = num // 10
    return count

print(count_digit(num))    
