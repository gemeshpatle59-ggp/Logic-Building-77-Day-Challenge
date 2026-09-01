# Find the smallest two distinct digits

num = 8768743

def smallest_distinct(num):
    digit = [float("inf"), float("inf")]  # [smallest, second_smallest]

    while num > 0:
        last_digit = num % 10

        if last_digit < digit[0]:
            digit[1] = digit[0]
            digit[0] = last_digit

        elif last_digit < digit[1] and last_digit != digit[0]:
            digit[1] = last_digit

        num = num // 10

    return digit


print(smallest_distinct(num))               