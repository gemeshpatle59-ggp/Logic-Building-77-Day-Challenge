#  Create a pattern using alternating 0 and 1 values


def alternating_0_1_pattern():

    try:
        n = int(input("ENTER YOUR LENGTH NUMBER HERE.: "))

        count = 1
        for k in range(1,n+1):
            if count % 2 == 0 :
                for i in range(1,k+1):
                    if i % 2 == 0:
                        print(1,end=" ")
                    else:
                        print(0, end=" ")

                print()
                count += 1
            else:
                for j in range(1,k+1):
                    if j % 2 == 0:
                        print(0 , end=" ")
                    else:
                        print(1 ,  end=" ")
                print()
                count += 1

            
    except ValueError:
        print("Invalid input! Please enter an Integer.")

if __name__ == "__main__":
    alternating_0_1_pattern()             