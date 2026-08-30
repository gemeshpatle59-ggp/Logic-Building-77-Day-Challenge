#  Reverse an integer without converting it to a string.

num = 894635


def reverse_integer(num):
    reverse_integer = 0

    while num > 0:
        digit = num % 10
        reverse_integer = reverse_integer*10 + digit
        num = num // 10

    return reverse_integer

print(reverse_integer(num))    

