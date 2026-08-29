#  Count the frequency of a particular digit.

num = 453663

def count_frequency(num):
    num = abs(num)

    freq = {}

    if num == 0:
        freq[num] = 1
        return freq

    while num > 0:
        last_digit = num % 10
        if last_digit in freq:
            freq[last_digit] += 1

        else:
            freq[last_digit] = 1

        num = num // 10

    return freq

print(count_frequency(num))            