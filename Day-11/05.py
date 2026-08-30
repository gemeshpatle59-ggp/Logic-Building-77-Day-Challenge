# Check whether an integer is a palindrome

num = 1221

def check_pelindrome(num):
    n = num

    reverse = 0

    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10

    if num == reverse:
        print(f"{num} is pelindrome")

    else:
        print(f"{num} is not a pelindrome")

check_pelindrome(num)            