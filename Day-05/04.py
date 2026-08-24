# 4.	Print all odd numbers from 1 to N.


def num():
    try:
        n = int(input("ENTER THE NUMBER HERE.: "))
        for i in range(n,1,-2):
            print(i)

    except ValueError:
        print("Please enter the valid number.")

if __name__ == "__main__":
    num()