# Find GCD/HCF of two numbers using a loop.

def find_hcf():
    try:
        n= int(input("ENTER YOUR 1st NUMBER HERE.: "))
        m= int(input("ENTER YOUR 2nd NUMBER HERE.: "))
        
        hcf = 0

        for i in range(1, min(n, m) + 1):
            if n % i == 0 and m % i == 0:
                hcf = i

        print(hcf)
                
    except ValueError:
        print("Invalid input! Please enter an Integer.")
    

if __name__ == "__main__":
    find_hcf()              