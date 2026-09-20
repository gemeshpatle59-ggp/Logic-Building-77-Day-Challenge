#  Check whether a number is prime using recursion

def check_prime(num ,i=2):
    if num == 1 or num == 0:
        return False
    if i == num:
        return True
    if num % i == 0:
        return False

    return check_prime(num , i+1)

print(check_prime(2))