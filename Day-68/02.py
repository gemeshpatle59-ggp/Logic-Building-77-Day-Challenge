# Dry-run a palindrome algorithm for 1221 and 1231.

def check_palindrome(num):

    n =  num
    palindrome = 0
    while n > 0:
        last_digit = n % 10
        palindrome = (palindrome * 10) + last_digit
        n = n // 10

    return num == palindrome

print(check_palindrome(1221))


"""
| Iteration |    n | digit = n % 10 | rev = rev * 10 + digit | n = n // 10 |
| --------- | ---: | -------------: | ---------------------: | ----------: |
| 1         | 1221 |              1 |                      1 |         122 |
| 2         |  122 |              2 |                     12 |          12 |
| 3         |   12 |              2 |                    122 |           1 |
| 4         |    1 |              1 |                   1221 |           0 |


"""