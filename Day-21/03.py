#  Convert decimal to octal manually.

def octal_num():
    try:
        n= int(input("ENTER YOUR NUMBER HERE.: "))

        octal = 0
        place = 1

        while n > 0:
            octal = (n % 8) * place + octal
            place = place * 10
            n = n//8

        
        print(f"octal = {octal}")


    except ValueError:
        print("Invalid input! Please enter an Integer.")
    

if __name__ == "__main__":
    octal_num()              