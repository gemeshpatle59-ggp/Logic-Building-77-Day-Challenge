# 4.	Check whether a character is uppercase or lowercase

def check_case():
    
    n = (input("ENTER THE CHARACTER HERE.: "))

    if "a" <= n <= "z":
        print(f"{n} is a lowercase character.")

    elif "A" <= n <= "Z":
        print(f"{n} is a uppercase character.")

    else:
        print(f"{n} is not a alphabate character.")

if __name__ == "__main__":
    check_case()        
                    