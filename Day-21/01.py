#  Convert decimal to binary without using bin()


def binary_num():
    try:
        n= int(input("ENTER YOUR NUMBER HERE.: "))

        binary = 0
        place = 1

        while n > 0:
            binary = (n % 2) * place + binary
            place = place * 10
            n = n//2

        
        print(f"binary = {binary}")


    except ValueError:
        print("Invalid input! Please enter an Integer.")
    

if __name__ == "__main__":
    binary_num()              