#  Print a diamond.

def diamond():
    try:
        n = int(input("ENTER YOUR LENGTH ONLY ODD NUMBER HERE.: "))

        for i in range(n//2):
           print(" "*(((n//2))-i) + (("*")*((i*2)+n)))

        for _ in range((n//2)//2):
            print("*" * (n*2-1))

        for k in range(n):
            print(" "*(k) + ("*" * (((n-k) * 2)-1)))

    except ValueError:
        print("Invalid input! Please enter an Integer.")
    

if __name__ == "__main__":
    diamond()              