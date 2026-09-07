#  Check whether two numbers are co-prime.

def check_two_number_coprime():
    try:
        n= int(input("ENTER YOUR 1st NUMBER HERE.: "))
        m= int(input("ENTER YOUR 2nd NUMBER HERE.: "))
        
        while m != 0:
            n,m = m,n%m

        if n != 1:
            print("Numbert is not coprime")
        else:
            print("Number is coprime")

    except ValueError:
        print("Invalid input! Please enter an Integer.")
    

if __name__ == "__main__":
    check_two_number_coprime()              