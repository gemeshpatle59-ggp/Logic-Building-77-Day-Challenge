# Check whether a number is a spy number

def check_spy():
    try:
        num = int(input("ENTER YOUR NUMBER HERE.: "))
        n = num
        total = 0
        product = 1

        while n > 0:
            last_digit = n % 10
            total = total + last_digit
            product = product * last_digit
            n = n // 10

        if total == product:
            return True
        else:
            return False

    except ValueError:
        print("Invalid input! Please enter an Integer.")
    

if __name__ == "__main__":
    print(check_spy())              