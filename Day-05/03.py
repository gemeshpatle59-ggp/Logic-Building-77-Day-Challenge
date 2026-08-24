# 3.	Print all even numbers from 1 to N

def num():
    try:
        n = int(input("ENTER THE NUMBER HERE.: "))
        for i in range(2,n+1,2):
            print(i)

    except ValueError:
        print("Please enter the valid number.")

if __name__ == "__main__":
    num()