# 5.	Find the smallest number among N inputs

def Smallest_number():

    try:
        n = int(input("HOW MANY NUMBER YOU WANT TO ENTER.: "))

        if n <= 0:
            print("Please enter a number greater than 0.")
            return
        

        number = float("inf")

        for i in range(1,n+1):
            m = int(input("ENTER THE NUMBER HERE.: "))    
            if number >= m:
                number = m

        print(f"Smallest number is {number}")

    except ValueError:
        print("Please enter the valid number..")     

if __name__ == "__main__":
    Smallest_number()  