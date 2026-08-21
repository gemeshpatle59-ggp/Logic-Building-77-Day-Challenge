# 1.	Find the smallest of three numbers

def maxm():

    while True:
    
        try:
            n = int(input("ENTER THE 1ST NUMBER HERE.: "))
            m = int(input("ENTER THE 2ND NUMBER HERE.: "))
            o = int(input("ENTER THE 3RD NUMBER HERE.: "))
    
            if n < m and n < o:
                 print(f"{n} is smallest of the three number.")
                 break

            elif m < n and m < o:
                 print(f"{m} is smallest of the three number.")     
                 break
            else:
                 print(f"{o} is smallest of the three number.")     
                 break                   
    
        except ValueError:
                print("Please enter the number only.:")    
    
if __name__ == "__main__":
    maxm()           