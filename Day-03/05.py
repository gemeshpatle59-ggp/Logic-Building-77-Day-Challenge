# 5.	Check whether a number lies inside a given range.

def check_range():
    try:
        n = int(input("ENTER THE NUMBER HERE.: "))
        m = int(input("ENTER THE STARTING RANGE HERE.: "))
        o = int(input("ENTER THE ENDING RANGE HERE.: "))

        if m <= n <= o:
            print(f"The number {n} lies in range {m} to {o}")
        else:
            print(f"The number {n} not lies in a range {m} to {o}")
        
            
    except ValueError:
        print("Please enter valid numbers.")


if __name__ == "__main__":
    check_range()