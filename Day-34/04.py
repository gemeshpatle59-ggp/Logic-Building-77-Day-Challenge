# Trace every recursive call for factorial, digit sum, and reverse-number problems by hand.

def factorial(facts):
    if facts == 0:
        return 1
    if facts == 1:
        return 1


    return factorial(facts -1) * facts 

print(factorial(5))


def digit_sum(num , j=0):
    if num == 0:
        return j

    last_digit = num % 10
    j += last_digit

    return digit_sum(num//10,j)

print(digit_sum(123))
        