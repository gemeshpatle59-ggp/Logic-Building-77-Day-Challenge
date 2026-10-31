# Find and fix a program that fails for negative integers.

num = int(input("Enter a number: "))

while num > 0:
    digit = num % 10
    print(digit)
    num //= 10


num = int(input("Enter a number: "))

num = abs(num)

while num > 0:
    digit = num % 10
    print(digit)
    num //= 10
