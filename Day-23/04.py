#  Print a hollow square.


def diamond():
    try:
        n = int(input("ENTER YOUR LENGTH ONLY ODD NUMBER HERE.: "))

        print("* " * n)

        for i in range((n//2)):
            print("* " + ("  " * ((n-2)  )) + "*")

        print("* " * n)

    except ValueError:
        print("Invalid input! Please enter an Integer.")
    

if __name__ == "__main__":
    diamond()              