#  Print an inverted centered pyramid.

def invertedcenteredpyramid():
    try:
        n = int(input("ENTER YOUR LENGTH HERE.: "))

        for i in range(n):
           print(" "*(i) + "*"*(((n-i)*2)-1))


    except ValueError:
        print("Invalid input! Please enter an Integer.")
    

if __name__ == "__main__":
    invertedcenteredpyramid()              