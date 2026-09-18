#  Rewrite one previous program using helper functions to reduce repeated code.

"""
def get_number() ,,   
is a helper function to reduce the repeated input code in the program ...

"""

def get_number():
    return int(input("ENTER THE NUMBER HERE.: "))

def even_odd(num):

    return num % 2 == 0

def check_prime(num):

    if num < 2:
        return False

    for i in range(2,int(num ** 0.5)+1):
        if num % i == 0:
            return False

    return True

def factorial(num):

    if num < 0:
        return "Factorial is not defined for negative numbers"
    fact = 1
    for i in range(1,num+1):
        fact *= i
    return fact

def sum_of_digit(num):
    n = abs(num)
    total = 0
    while n > 0:
        last_digit = n % 10
        total += last_digit
        n = n // 10
    return total


while True:

    print("\n===== Number Toolkit =====\n")
    print("1. Check Even/Odd")
    print("2. Check Prime")
    print("3. Find Factorial")
    print("4. Find Sum of Digits")
    print("5. Exit ")


    try:
        choice = int(input("enter your choice (1/5) : "))


        if choice == 1:
            n = get_number()
            print(even_odd(n))

        elif choice == 2:
            m = get_number()

            print(check_prime(m))

        elif choice == 3:
            o = get_number()
            print(factorial(o))

        elif choice == 4:
            l = get_number()
            print(sum_of_digit(l))

        elif choice == 5:
            print("PROGRAM END")
            break
        else:
            print("Please choose input between (1/5)")

    except ValueError:
        print("please enter the integre in input")
