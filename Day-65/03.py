# Find the smallest number that is divisible by every integer from 1 to N.


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def smallest_divisible(n):
    result = 1

    for i in range(2, n + 1):
        result = (result * i) // gcd(result, i)

    return result


print(smallest_divisible(5)) 