# Take a digit-sum program and manually trace every value of n and result for 583


def digit_sum(n):
    result = 0

    while n > 0:
        digit = n % 10
        result = result + digit
        n = n // 10

    return result

print(digit_sum(538))