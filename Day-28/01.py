#   Write a function to check palindrome.

def check_palindrome(n):
    num = n
    new_num = 0

    while num > 0:
        last_digit = num % 10
        new_num = (new_num * 10) + last_digit
        num = num // 10

    return n == new_num

print(check_palindrome(12321))
