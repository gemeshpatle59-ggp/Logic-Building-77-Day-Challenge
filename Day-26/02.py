#  For a given N, print a pattern where each row contains increasing numbers followed by decreasing numbers.


def increasingnumberfollowdecreasingnumber():
    try:
        n = int(input("ENTER YOUR LENGTH NUMBER HERE.: "))

        for i in range(1,n+1):
            for j in range(1,i+1):
                print(j, end=" ")

            for j in range(i-1,0,-1):
                print(j , end=" ")

            print()
            

    except ValueError:
        print("Invalid input! Please enter an Integer.")

if __name__ == "__main__":
    increasingnumberfollowdecreasingnumber()             