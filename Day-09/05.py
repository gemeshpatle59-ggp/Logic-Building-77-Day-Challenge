# Find the largest digit

num = -453

def largest_digit(num):
    num = abs(num)

    largest = 0
    while num > 0:
        last_digit = num % 10
        if largest < last_digit:
            largest = last_digit
        num = num // 10
        
    return largest

print(largest_digit(num))    