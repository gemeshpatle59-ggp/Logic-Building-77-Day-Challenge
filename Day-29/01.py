# 1. Write a function to check Armstrong.

def armstrong(num):
    n = num

    total = 0

    while n > 0:
        last_digit = n % 10
        total += last_digit**(len(str(num)))
        n = n // 10

    return total == num

print(armstrong(153))
