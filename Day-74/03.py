"""
Build a menu-driven math toolkit using functions for prime, factors, GCD, LCM, Armstrong, palindrome, and
digit operations.

"""

# 1. Prime Number
def prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


# 2. Factors
def factors(n):
    print("Factors:", end=" ")

    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=" ")

    print()


# 3. GCD
def gcd(a, b):
    while b != 0:
        a, b = b, a % b

    return a


# 4. LCM
def lcm(a, b):
    return abs(a * b) // gcd(a, b)


# 5. Armstrong Number
def armstrong(n):
    temp = n
    power = len(str(n))
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** power
        temp //= 10

    return total == n


# 6. Palindrome Number
def palindrome(n):
    temp = n
    rev = 0

    while temp > 0:
        digit = temp % 10
        rev = rev * 10 + digit
        temp //= 10

    return rev == n


# 7. Digit Operations
def digit_operations(n):
    temp = abs(n)
    total = 0
    count = 0
    rev = 0

    while temp > 0:
        digit = temp % 10

        total += digit
        count += 1
        rev = rev * 10 + digit

        temp //= 10

    print("Digit Count:", count)
    print("Digit Sum:", total)
    print("Reverse:", rev)


# Main Menu
while True:

    print("\n===== MATH TOOLKIT =====")
    print("1. Prime Number")
    print("2. Factors")
    print("3. GCD")
    print("4. LCM")
    print("5. Armstrong Number")
    print("6. Palindrome Number")
    print("7. Digit Operations")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        n = int(input("Enter number: "))

        if prime(n):
            print("Prime Number")
        else:
            print("Not Prime")

    elif choice == 2:
        n = int(input("Enter number: "))
        factors(n)

    elif choice == 3:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("GCD:", gcd(a, b))

    elif choice == 4:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("LCM:", lcm(a, b))

    elif choice == 5:
        n = int(input("Enter number: "))

        if armstrong(n):
            print("Armstrong Number")
        else:
            print("Not Armstrong")

    elif choice == 6:
        n = int(input("Enter number: "))

        if palindrome(n):
            print("Palindrome Number")
        else:
            print("Not Palindrome")

    elif choice == 7:
        n = int(input("Enter number: "))
        digit_operations(n)

    elif choice == 8:
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")