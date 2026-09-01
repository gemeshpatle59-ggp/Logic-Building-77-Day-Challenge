#  Check whether a number contains a given digit.

num = 57265
n = 2

def check_number_in_digit(num, n):

    for digit in str(num):
        if str(n) == digit:
            print(f"{num} contains the given digit {n}")
            return

    print(f"{num} does not contain the given digit {n}")

check_number_in_digit(num, n)