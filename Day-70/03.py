# Rewrite five programs without using built-in functions that directly solve the main task.

n = 17
is_prime = True

if n < 2:
    is_prime = False
else:
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

if is_prime:
    print("Prime")
else:
    print("Not Prime")


n = 583
count = 0

if n == 0:
    count = 1

while n > 0:
    count += 1
    n //= 10

print(count)

arr = [12, 45, 7, 89, 23]

largest = arr[0]

for num in arr:
    if num > largest:
        largest = num

print(largest)

n = 1234
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n //= 10

print(rev)


arr = [10, 20, 30, 40]
total = 0

for num in arr:
    total += num

print(total)