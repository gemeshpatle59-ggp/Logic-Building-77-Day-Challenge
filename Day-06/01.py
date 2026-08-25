# 1.	Find the sum of numbers from 1 to N.

def sum():

    try:

        n = int(input("ENTER THE NUMBER HERE.: "))

        sum = 0

        for i in range(1,n+1):
            sum += i

        print(sum)

    except ValueError:
        print("please enter the valid number.")

if __name__ == "__main__":
    sum()        