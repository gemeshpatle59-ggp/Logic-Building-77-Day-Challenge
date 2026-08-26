# 3.	Find the average of N entered numbers.


def average():

    try:
        n = int(input("HOW MANY NUMBER YOU WANT TO ENTER.: "))

        if n <= 0:
            print("Please enter a number greater than 0.")
            return

        number = 0

        for i in range(1,n+1):
            m = int(input("ENTER THE NUMBER HERE.: "))
            number += m

        average = number/n

        print(f"Average {average}")

    except ValueError:
        print("Please enter the valid number..")     

if __name__ == "__main__":
    average()        