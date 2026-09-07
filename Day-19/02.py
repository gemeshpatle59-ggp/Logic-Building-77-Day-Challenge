#  Find GCD using the Euclidean algorithm

def find_gcd_Euclidean_algorithm():
    try:
        n= int(input("ENTER YOUR 1st NUMBER HERE.: "))
        m= int(input("ENTER YOUR 2nd NUMBER HERE.: "))
        
        while m != 0:
            n,m = m,n%m
            
        print("GCD =",n)

    except ValueError:
        print("Invalid input! Please enter an Integer.")
    

if __name__ == "__main__":
    find_gcd_Euclidean_algorithm()              