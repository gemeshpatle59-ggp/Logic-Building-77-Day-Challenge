# Check palindrome recursively using a helper approach.

def check_palindrome(num, m = 0):
    if num == 0:
        return m

    last = num % 10
    m = m * 10 + last
    return check_palindrome(num // 10 , m)

def is_palindrome(num):
    return num == check_palindrome(num)

print(is_palindrome(12321))