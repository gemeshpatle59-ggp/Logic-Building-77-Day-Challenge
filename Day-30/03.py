# Create functions for decimal/binary conversion and test them against edge cases.


def decimal_to_binary(num):
    binary = ""

    n = num
    if n == 0:
        return "0"

    while n > 0:
        temp = n % 2
        binary = str(temp) + binary
        n = n // 2

    return int(binary)

print(decimal_to_binary(4))