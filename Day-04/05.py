# 5.	Create a menu-driven program for basic arithmetic operations

def menu_bar():

    print("1. TO Addition")
    print("2. TO Subtraction")
    print("3. TO Multiplication")
    print("4. TO Division")
    print("5. TO EXIT")
    while True:

        try:
            choice = int(input("ENTER YOUR CHOICE FROM (1 TO 5)."))

            if choice == 1:
                n = int(input("ENTER THE 1ST NUMBER HERE."))
                m = int(input("ENTER THE 2ND NUMBER HERE."))
                print("---ADDITION---")
                print(f"\n{n} + {m} = {n+m}")

            elif choice == 2:
                n = int(input("ENTER THE 1ST NUMBER HERE."))
                m = int(input("ENTER THE 2ND NUMBER HERE."))
                print("---SUBTRACTION---")  
                print(f"\n{n} - {m} = {n-m}") 

            elif choice == 3:
                n = int(input("ENTER THE 1ST NUMBER HERE."))
                m = int(input("ENTER THE 2ND NUMBER HERE."))         
                print("---MULTIPLICATION---")
                print(f"\n{n} x {m} = {n*m}")

            elif choice == 4:
                n = int(input("ENTER THE 1ST NUMBER HERE."))
                m = int(input("ENTER THE 2ND NUMBER HERE."))    
                print("---DIVISION---")
                print(f"\n{n}/{m} = {n/m:.2f}")

            else:
                break    
        except ValueError:
            print("Please enter the valid number or choice..")    


if __name__ == "__main__" :
    menu_bar()           