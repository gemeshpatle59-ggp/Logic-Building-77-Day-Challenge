# Check whether a number is a palindrome using only arithmetic operations

def chech_palindrome():

    n = int(input("Enter a number here.: "))
    num = n
    palindrome = 0


    while num > 0:
        last_digit = num % 10
        palindrome = (palindrome * 10) + last_digit
        num = num // 10

    return palindrome == n


print(chech_palindrome())
