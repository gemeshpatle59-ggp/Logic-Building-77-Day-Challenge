# Count how many digits are even.

num = 7364812937812965


def count_even(num):
    even = 0
    num = abs(num)

    while num > 0:
        last_digit = num % 10
        if last_digit % 2 == 0:
            even += 1
        num = num // 10    

    return even

print(f"Total Even digit are {count_even(num)}")        