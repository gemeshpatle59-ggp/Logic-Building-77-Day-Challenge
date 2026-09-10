#  Print a rectangle of stars.

def square_star():
    try:
        n = int(input("ENTER YOUR LENGTH  HERE.: "))
        m = int(input("ENTER YOUR BREDTH  HERE.: "))
        

        for _ in range(m):
           print("* "*n)


    except ValueError:
        print("Invalid input! Please enter an Integer.")
    

if __name__ == "__main__":
    square_star()              