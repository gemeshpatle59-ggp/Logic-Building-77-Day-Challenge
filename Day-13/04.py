#  Find the second largest digit.

# Find the largest two distinct digits

num = 76438

def two_distinct(num):
    digit = [-1, -1]   # [largest, second_largest]

    while num > 0:
        last_digit = num % 10

        if last_digit > digit[0]:
            digit[1] = digit[0]
            digit[0] = last_digit

        elif last_digit > digit[1] and last_digit != digit[0]:
            digit[1] = last_digit

        num = num // 10

    return digit[1]


print(two_distinct(num))