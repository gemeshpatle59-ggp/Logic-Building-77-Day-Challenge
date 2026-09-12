#  Print a hollow triangle.

def hallowtriangle():
    try:
        n = int(input("ENTER YOUR LENGTH ONLY ODD NUMBER HERE.: "))

        for i in range(n):
            print(" " * (n-i) + ("*") + (" " * ((2*i)-1)) , end="")
            if i > 0:
                print("*" , end="")
            print()

        print("* "*(n+1))
    except ValueError:
        print("Invalid input! Please enter an Integer.")
    

if __name__ == "__main__":
    hallowtriangle()              