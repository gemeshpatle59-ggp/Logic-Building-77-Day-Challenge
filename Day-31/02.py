# Find sum of 1 to N recursively.

def sum_of_one_to_n(n):
    if n == 0:
        return 0
    return sum_of_one_to_n(n-1) + n

print(sum_of_one_to_n(3))