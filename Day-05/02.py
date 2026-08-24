# 2.	Print numbers from N to 1.

def num():
    try:
        n = int(input("ENTER THE NUMBER HERE.: "))
        for i in range(n,0,-1):
            print(i)

    except ValueError:
        print("Please enter the valid number.")

if __name__ == "__main__":
    num()