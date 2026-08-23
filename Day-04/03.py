# 3.	Check whether the sum of two numbers is even or odd.

def check_sum():
    try:
            n = int(input("ENTER THE 1ST NUMBER HERE.: "))
            m = int(input("ENTER THE 2ND NUMBER HERE.: "))
    
            if (n+m) % 2 == 0:
                 print("The sum of two number is EVEN.")

            else:
                 print("The sum of two number is ODD.")        
    
    except ValueError:
        print("Please enter the valid number in input.")

if __name__ == "__main__":
     check_sum()