# 3.	Check whether a character is an alphabet, digit, or special character

def check():
    try:
        n = (input("ENTER THE YEAR HERE.: "))

        if "a" <= n <= "z" or "A" <= n <= "Z":
            print(f"{n} is alphabet character")

        elif "0" <= n <= "9":
            print(f"{n} is digit")

        else:
            print(f"{n} is a special character")

                                
    except ValueError:
        print("Please enyter the valid year..")            

if __name__ == "__main__":
    check()