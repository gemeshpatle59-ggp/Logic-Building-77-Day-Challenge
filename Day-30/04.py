#  Write a function that validates an integer before performing digit operations.


def validate_integer(num):
    try:
        return int(num)
    except ValueError:
        return None


def sum_of_digits(num):
    total = 0

    num = abs(num)

    while num > 0:
        digit = num % 10
        total += digit
        num //= 10

    return total


num = input("Enter an integer: ")

valid_num = validate_integer(num)

if valid_num is not None:
    print(sum_of_digits(valid_num))
else:
    print("Invalid integer")