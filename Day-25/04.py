#  Print a checkerboard pattern.

def invertedalphabettriangle():
    try:
        n = int(input("ENTER YOUR LENGTH NUMBER HERE.: "))

        for i in range(1,n+1):
            if i % 2 == 0:
                print(" "+ "* "*n)
            else:
                print("* "*n)

    except ValueError:
        print("Invalid input! Please enter an Integer.")

if __name__ == "__main__":
    invertedalphabettriangle()              