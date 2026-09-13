#  Print a butterfly pattern.

def butterflypattern():
    try:
        n = int(input("ENTER YOUR LENGTH NUMBER HERE.: "))

        for i in range(1,(n//2)+2):
            print("*"*i + (" "*((n*2)-(i+i))) + ("*"*i))

        for _ in range((n//2)//2):
            print("*"*(n*2))

        for j in range((n//2)+1,0,-1):
            print("*"*j + (" "*((n*2)-(j+j))) + ("*"*j))


    except ValueError:
        print("Invalid input! Please enter an Integer.")

if __name__ == "__main__":
    butterflypattern()             