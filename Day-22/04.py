#  Print a right-angled triangle.

def rightangletriangle():
    try:
        n = int(input("ENTER YOUR LENGTH HERE.: "))

        for i in range(n):
           print("* "*(i))


    except ValueError:
        print("Invalid input! Please enter an Integer.")
    

if __name__ == "__main__":
    rightangletriangle()              