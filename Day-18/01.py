#  Check whether a number is a neon number.

def check_neon():
    try:
        num = int(input("ENTER YOUR NUMBER HERE.: "))
        n = num ** 2
        total = 0
        while n > 0:
            last_digit = n % 10
            total = total + last_digit
            n = n // 10

        if num == total:
            print(f"{num} is a neon number.")
        else:
            print(f"{num} is not a neon number..")


    except ValueError:
        print("Invalid input! Please enter an Integer.")
    

if __name__ == "__main__":
    check_neon()                