# 5.	Print multiples of K up to N.

def multiple():
    try:
        k = int(input("ENTER THE NUMBER HERE.: "))
        n = int(input("ENTER YOUR RANGE HERE.: "))

        for i in range(1,n+1):
            if k % i == 0:
                print(i)


    except ValueError:
        print("Please enter the valid number.")

if __name__ == "__main__":
    multiple()