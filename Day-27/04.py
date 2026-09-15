#  Write a function to count digits.


def count_digit(n):
    num = n
    count = 0

    while num > 0:
        count += 1
        num = num // 10

    return ("Total digit in number is", count )

print(count_digit(18761287))