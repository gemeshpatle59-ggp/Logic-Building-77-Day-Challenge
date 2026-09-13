#  Print an inverted alphabet triangle.

def invertedalphabettriangle():
    try:
        n = int(input("ENTER YOUR LENGTH NUMBER HERE.: "))
        m = n * (n + 1) // 2
        for k in range(n,0,-1):
            h = m
            l = h - k 
            for j in range(h,l,-1):
                print(chr(64+j) , end=" ") 
            m = l
            print()

    except ValueError:
        print("Invalid input! Please enter an Integer.")

if __name__ == "__main__":
    invertedalphabettriangle()              