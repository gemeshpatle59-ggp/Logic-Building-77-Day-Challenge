# Count how many digits are odd


num = 4567

def count_odd(num):
    odd = 0
    num = abs(num)

    while num > 0:
        last_digit = num % 10
        if last_digit % 2 != 0:
            odd += 1
        num = num // 10    

    return odd

print(f"Total odd digit are {count_odd(num)}")        