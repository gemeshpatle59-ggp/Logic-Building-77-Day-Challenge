#  Find the sum of digits at even positions and odd positions.

num = 872389

def sum_even_odd(num):
    even = 0
    odd = 0

    while num > 0:
        last_digit = num % 10
        if last_digit % 2 == 0:
            even += last_digit
        else:
            odd += last_digit

        num = num // 10

    print(f"\nsum of even is {even} and odd is {odd}\n")

sum_even_odd(num)            