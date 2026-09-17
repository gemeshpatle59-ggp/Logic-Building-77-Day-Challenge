# 4. Create a function that returns multiple results instead of printing them.

def multiple_return(num):

    total_digit = 0
    total = 0
    n = num

    while n > 0:
        last_digit = n % 10
        total_digit += 1
        total += last_digit
        n = n // 10

    return total_digit , total

digits, digit_sum = multiple_return(12343)

print("total_digit =", digits)
print("sum of all digit =", digit_sum)