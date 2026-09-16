# 5. Write a function to calculate LCM using GCD

def lcm_using_gcd(a,b):
    n = b
    m = a
    while n != 0:
        m, n = n, m % n

    lcm = (a * b) / m
    return "lcm using gcd is " ,lcm

print(lcm_using_gcd(12 , 18))