# Convert decimal to hexadecimal manually.

def hexadecimal():
    try:
        n= int(input("ENTER YOUR NUMBER HERE.: "))

        digits = "0123456789ABCDEF"

        if n == 0:
            return "0"

        result = ""

        while n > 0:
            remainder = n % 16
            result = digits[remainder] + result
            n = n // 16

        print(result)


    except ValueError:
        print("Invalid input! Please enter an Integer.")
    

if __name__ == "__main__":
    hexadecimal()              