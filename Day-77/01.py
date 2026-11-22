#  Find the sum of all digits that occur exactly once.


def sum_of_digits_occur_once(nums):

    freq = {}
    total = 0

    while nums > 0:
        last_digit = nums % 10

        if last_digit not in freq:
            freq[last_digit] = 1
            total += last_digit

        elif freq[last_digit] == 1:
            freq[last_digit] += 1
            total -= last_digit

        else:
            freq[last_digit] += 1

        nums //= 10

    return total


print(sum_of_digits_occur_once(1122344556677899))
# Output: 11