# 1.	Find the middle value among three distinct numbers 

def distinct():
    
    try:
        n = int(input("ENTER THE NUMBER HERE.: "))
        m = int(input("ENTER THE NUMBER HERE.: "))
        o = int(input("ENTER THE NUMBER HERE.: "))

        if m < n < o or o < n < m:
            print(f"distinct number is {n}")

        elif n < m < o or o < m < n:
            print(f"distinct number is {m}")
        else:
            print(f"distinct number is { o}")

    except ValueError:
        print("Please enter the valid number in input") 

if __name__ == "__main__":
    distinct()                       