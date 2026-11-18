#  Create a basic ATM simulation using functions, conditions, loops, and dictionaries.

import random

def Atm():

    print("-----------------------------")
    print("-------WELCOME TO ATM--------")
    print("-----------------------------\n")

    card_no = 1234
    attemp = 3
    while attemp > 0:

        try:
            card = int(input("Enter the card number here.: "))

            if card == card_no:
                print("Login Successful")
                break

            else:
                print("Wrong_pin.. 2 attemp left")

            attemp -= 1

        except ValueError:
            print("Please enter a pin in interger form")

    balance = random.randint(1,10000)

    print("1.TO CHECK BALANCE")
    print("2.TO WITHDRAW AMOUNT")
    print("3.TO DEPOSITE AMOUNT")
    print("4.TO QUIT")


    while True:

        try:

            choice = int(input("ENTER YOUR CHOICE HERE.: "))

            if choice == 1:

                print(f"balance  = {balance:.2f}")

            elif choice == 2:
                while True:
                    try:
                        withdraw = int(input("Enter a amount to witdraw.: "))

                        if withdraw > balance:
                            print(f"insufficent balance current balance is {balance:.2f}")

                        elif withdraw < 0:
                            print("withdraw balance cant be negative")

                        else:
                            balance = balance - withdraw

                            print(f"Withdraw successful.... current balance is {balance:.2f}")

                            break

                    except ValueError:
                        print("please enter the integer value in withdraw amount")


            elif choice == 3:
                while True:
                    try:
                        withdraw = int(input("Enter a amount to witdraw.: "))

                        if withdraw < 0:
                            print("deposite balance cant be negative")

                        else:
                            balance = balance + withdraw

                            print(f"deposite successful.... current balance is {balance:.2f}")

                            break

                    except ValueError:
                        print("please enter the integer value in withdraw amount")


            elif choice == 4:
                print("----------------------------")
                print("--------THANK YOU ----------")
                print("----------------------------")
                break

            else:
                print("please enter the choice from (1 to 4)")

        except ValueError:
            print("Please enter the integer value")


if __name__ == "__main__":
    Atm()


            

    


