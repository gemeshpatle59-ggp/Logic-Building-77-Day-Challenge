# 5. Separate input, processing, and output into different functions


def get_input():
    num = int(input("Enter number: "))
    return num


def calculate(num):
    total = 0

    while num > 0:
        total += num % 10
        num //= 10

    return total


def show_output(result):
    print("Sum =", result)


num = get_input()
result = calculate(num)
show_output(result)