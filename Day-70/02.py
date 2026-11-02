# For five previous programs, predict the output before executing them.

# Program 1: Sum of digits
n = 583
total = 0

while n > 0:
    total += n % 10
    n //= 10

print(total)  # 16

# Program 2: Reverse a number
n = 1200
rev = 0

while n > 0:
    rev = rev * 10 + n % 10
    n //= 10

print(rev)  # 21

# Program 3: Factorial
n = 5
fact = 1

for i in range(1, n + 1):
    fact *= i

print(fact)  # 120

# Program 4: Count digits
n = 12345
count = 0

while n > 0:
    count += 1
    n //= 10

print(count)  # 5

# Program 5: Check palindrome
n = 121
original = n
rev = 0

while n > 0:
    rev = rev * 10 + n % 10
    n //= 10

print(original == rev)  # True