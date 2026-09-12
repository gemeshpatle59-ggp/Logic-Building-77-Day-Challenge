#  Print a hollow rectangle

def hollowrectangle():
    try:
        n = int(input("ENTER YOUR LENGTH ONLY ODD NUMBER HERE.: "))

        print("* " * n)

        for i in range((n)):
            print("* " + ("  " * ((n-2)  )) + "*")

        print("* " * n)

    except ValueError:
        print("Invalid input! Please enter an Integer.")
    

if __name__ == "__main__":
    hollowrectangle()              