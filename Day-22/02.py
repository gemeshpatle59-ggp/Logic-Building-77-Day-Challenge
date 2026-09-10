#  Print a square of stars.

def square_star():
    try:
        n = int(input("ENTER YOUR LENGTH OF SIDE HERE.: "))

        for _ in range(n):
           print("* "*n)

    except ValueError:
        print("Invalid input! Please enter an Integer.")
    

if __name__ == "__main__":
    square_star()              