# Find the number formed after removing all occurrences of a given digit.

num = 67478942249004224
n = 4

def new_number(num, n):
    num = str(num)
    result = ""

    for digit in num:
        if digit != str(n):
            result += digit

    print(int(result))

new_number(num, n)