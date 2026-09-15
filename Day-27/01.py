# 1. Recreate five different patterns using only nested loops and no string multiplication

def five_different_pattern():
    try:
        n = int(input("ENTER YOUR LENGTH NUMBER HERE.: "))

        for i in range(n):
            for _ in range(n):
                print("*" , end=" ")
            print()

        print()

        for j in range(n):
            for _ in range(n*2):
                print("*" , end=" ")
            print()

        print()
        
        for k in range(1,n+1):
            for _ in range(1,k+1):
                print("*" , end=" ")
            print()

        print("\n")

        for l in range(n,0,-1):
            for _ in range(l,0,-1):
                print("*" , end=" " )
            print()

    except ValueError:
        print("Invalid input! Please enter an Integer.")

if __name__ == "__main__":
    five_different_pattern()             