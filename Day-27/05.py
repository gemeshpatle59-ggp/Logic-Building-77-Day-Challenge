#  Write a function to reverse a number

def reverse_num(n):
    num = n
    reverse_num = 0
    while num > 0:
        last_digit = num % 10
        reverse_num = (reverse_num * 10) + last_digit
        num = num // 10

    return reverse_num

print(reverse_num(678))
