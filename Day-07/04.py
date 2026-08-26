# 4.	Find the largest number among N inputs.

def Larger_number():

    try:
        n = int(input("HOW MANY NUMBER YOU WANT TO ENTER.: "))

        if n <= 0:
            print("Please enter a number greater than 0.")
            return
        

        number = 0

        for i in range(1,n+1):
            m = int(input("ENTER THE NUMBER HERE.: "))
            if number <= m:
                number = m

        print(f"Largesr number is {number}")

    except ValueError:
        print("Please enter the valid number..")     

if __name__ == "__main__":
    Larger_number()        