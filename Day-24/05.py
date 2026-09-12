#  Print Floyd's triangle.

def floydstriangle():
    try:
        n = int(input("ENTER YOUR LENGTH ONLY ODD NUMBER HERE.: "))
        m = 0
        for i in range(1,n+1):
            m += i

            for j in range(1,m+1):
                print(j ,end=" ")
            print()

    except ValueError:
        print("Invalid input! Please enter an Integer.")

if __name__ == "__main__":
    floydstriangle()              