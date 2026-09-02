# Check whether a number is prime.

num = 5

def prime_num(num):

    if num < 2:
        print(f"{num} is a prime number")
        return

    for i in range(2,(num//2) +1):
        if num % i == 0:
            print(f"{num} is not a prime number")
            return
            

    print(f"{num} is a prime number")

prime_num(num)
