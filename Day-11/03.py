# Find the second-last digit of a number.

num = 7645847589

def second_last_digit(num):
    n = len(str(num))

    for i in range(2):
        last_digit = num % 10
        num = num // 10

    return last_digit

print(second_last_digit(num))    