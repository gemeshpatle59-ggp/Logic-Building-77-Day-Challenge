# 3. Create a reusable function that counts a chosen digit.

def countdigit(num,c):

    total_digit = 0
    n = num

    if num == 0:
        return 1 if c == 0 else 0

    while n > 0:
        last_digit = n % 10
        if last_digit == c:
            total_digit += 1
        n = n // 10

    return total_digit

print(countdigit(1223332,3))
