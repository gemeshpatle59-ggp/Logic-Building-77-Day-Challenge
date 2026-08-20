# 4.	Find the greater of two numbers without using max().

def maxm():

    while True:
    
        try:
            n = int(input("ENTER THE 1ST NUMBER HERE.: "))
            m = int(input("ENTER THE 2ND NUMBER HERE.: "))
    
            if n > m:
                 print(f"{n} is greater of the two number.")

            else:
                 print(f"{m} is the greater of the two  number.")     
                                         
    
        except ValueError:
                print("Please enter the number only.:")    
    
if __name__ == "__main__":
    maxm()           