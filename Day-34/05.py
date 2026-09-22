#  For each recursive solution, identify the base case and recursive case explicitly.

def factorial(n):

    # Base Case:
    # Jab n = 0 ya 1 ho, recursion yahi ruk jayega
    if n == 0 or n == 1:
        return 1

    # Recursive Case:
    # Function khud ko n-1 ke saath call kar raha hai
    return n * factorial(n - 1)


print(factorial(5))