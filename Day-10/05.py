# Count the frequency of every digit from 0 to 9.

num = 453663

def count_frequency(num):
    num = abs(num)

    freq = {}

    for i in range(10):
        freq[i] = 0

    while num > 0:
        last_digit = num % 10
        if last_digit in freq:
            freq[last_digit] += 1

        else:
            freq[last_digit] = 1

        num = num // 10

    return freq

print(count_frequency(num))            