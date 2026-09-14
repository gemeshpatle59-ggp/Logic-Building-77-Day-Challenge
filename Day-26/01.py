#  Print a hollow diamond.

def butterflypattern():
    try:
        n = int(input("ENTER YOUR LENGTH NUMBER HERE.: "))

        for i in range(n):
            print(" "*(n-1-i) + ("*") + (" "*((2*i)-1)) ,end="")
            if i > 0:
                print("*",end="")
            print()

        for i in range(1,n):
            print(" "*(i) + ("*") + (" "*(7-(2*i))) , end="")
            if i != n-1:
                print("*" , end="")
            print()

    except ValueError:
        print("Invalid input! Please enter an Integer.")

if __name__ == "__main__":
    butterflypattern()             