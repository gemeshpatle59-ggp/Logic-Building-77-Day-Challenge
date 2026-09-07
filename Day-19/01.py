#  Find LCM of two numbers.

def find_lcm():
    try:
        n= int(input("ENTER YOUR 1st NUMBER HERE.: "))
        m= int(input("ENTER YOUR 2nd NUMBER HERE.: "))
        
        lcm = max(n,m)

        while True:
            if lcm % n == 0 and lcm % m == 0:
                   break
            lcm += 1
            
        print(lcm)
    except ValueError:
        print("Invalid input! Please enter an Integer.")
    

if __name__ == "__main__":
    find_lcm()              