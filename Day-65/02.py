# Find the largest palindrome made from the product of two numbers under N.

def largest_palindrome(n):

    def check_palindrome(num):
        palindrome = 0
        k = num

        while k > 0:
            last_digit = k % 10
            palindrome = (palindrome * 10) + last_digit
            k = k // 10

        if palindrome == num:
            return True

        return False

    for i in range(n-1 , -1 , -1):
        for j in range(i , -1 , -1):
            k = i * j

            if check_palindrome(k) == True:
                return k


print(largest_palindrome(100))
