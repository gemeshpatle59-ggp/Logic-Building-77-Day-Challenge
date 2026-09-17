# 2. Write a function to check perfect number.

def perfect_number(num):

    total = 0

    for i in range(1,(num//2)+1):
        if num % i == 0:
            total += i

    return total == num

print(perfect_number(6))