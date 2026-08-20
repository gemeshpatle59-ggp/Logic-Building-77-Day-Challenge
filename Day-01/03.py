# 3.	Check whether one number is divisible by another

def divisible():

    while True:

        try:
            n = int(input("ENTER THE 1ST NUMBER HERE.: "))
            m = int(input("ENTER THE 2ND NUMBER HERE.: "))

            if n == 0 and m == 0:
                print("Both numbers are zero. Divisibility is not defined.")
                break

            elif m == 0:
                print("Cannot divide by zero.")
                break

            elif n == 0:
                print(f"{n} is divisible by {m}")
                break

            elif n % m == 0:
                print(f"{n} is divisible by {m}")
                break
            elif m % n == 0:
                print(f"{m} is divisible by {n}")
                break        
            else:
                print("Neither number is divisible by the other.")
                break

        except ValueError:
            print("Please enter the number only.:")    

if __name__ == "__main__":
    divisible()            