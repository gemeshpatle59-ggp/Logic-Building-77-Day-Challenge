#  Find the difference between the sum of even and odd digits.

num = 2343

def difference_even_odd(num):
    even = 0
    odd = 0
    while num > 0:
        last_digit = num % 10
        if last_digit % 2 == 0:
            even += last_digit
        else:
            odd += last_digit

        num = num//10

    difference = even - odd
    return difference

print(difference_even_odd(num))        