#  Write a function to calculate GCD.

def gcd(a,b):

    while b != 0:
        a , b = b, a%b
    return a

print(gcd(78,68))