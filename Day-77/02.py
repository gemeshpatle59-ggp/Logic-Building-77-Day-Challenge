# Find the count of distinct digits in an integer.

def distinct_digit(num):

    distinct = 0
    digits = [0,1,2,3,4,5,6,7,8,9,]

    while num > 0:
        x = num % 10

        if x in digits:
            distinct += 1
            digits.remove(x)

        num = num // 10

    return distinct

print(distinct_digit(1122345654345213454324554334355454))
