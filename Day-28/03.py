#  Write a function to return all factors.

def factors(num):

    for i in range(1,num//2 + 1):
        if num % i == 0:
            print(i , end=" ")

    print(num , end=" ")
    print()

factors(12)