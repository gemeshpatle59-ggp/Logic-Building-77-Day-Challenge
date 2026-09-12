#  Print repeated-number rows: 1 / 22 / 333 / ...

def repeated_number():
    try:
        n = int(input("ENTER YOUR LENGTH ONLY ODD NUMBER HERE.: "))

        for i in range(1,n+1):
            for j in range(1,i+1):
                print(i,end="")
            print()

    except ValueError:
        print("Invalid input! Please enter an Integer.")
    

if __name__ == "__main__":
    repeated_number()              