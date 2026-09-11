#  Print a centered pyramid

def centeredpyramid():
    try:
        n = int(input("ENTER YOUR LENGTH HERE.: "))

        for i in range(1,n+1):
           print(" "*(n-i) + "*"*((i*2)-1))


    except ValueError:
        print("Invalid input! Please enter an Integer.")
    

if __name__ == "__main__":
    centeredpyramid()              