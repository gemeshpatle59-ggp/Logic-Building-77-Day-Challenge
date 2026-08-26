# 2.	Find factorial of N using a loop.

def Factorial():

    try:

        n = int(input("ENTER THE NUMBER HERE.: "))

        fact = 1

        print("---Factorial_of",(n),"---")

        for i in range(1,n+1):
            fact *= i

        print(f"fact = {fact}")


    except ValueError:
        print("please enter the valid number.")

if __name__ == "__main__":
    Factorial()        