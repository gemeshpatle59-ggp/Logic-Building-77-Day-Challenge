# Find all palindromic numbers in a range.

def find_pelindrome(start , end):

    for i in range(start , end):
        j = i
        p = 0
        while j > 0:
            last_digit = j % 10
            p = (p * 10) + last_digit
            j = j // 10

        if i == p:
            print(i)

find_pelindrome(10 , 100)