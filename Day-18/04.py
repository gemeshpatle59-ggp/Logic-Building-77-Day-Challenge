#  Check whether a number is a duck number

def check_duck():
    try:
        n= (input("ENTER YOUR NUMBER HERE.: "))
    
        if n[0] == "0":
            return False
        elif "0" in n:
            return True
        else:
            return False

    except ValueError:
        print("Invalid input! Please enter an Integer.")
    

if __name__ == "__main__":
    print(check_duck())              