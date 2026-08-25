
# 2.	Find the sum of all even numbers from 1 to N.

def sum():
    try:

        n = int(input("ENTER THE NUMBER HERE.: "))

        sum = 0

        for i in range(2,n+1,2):
            sum += i

        print(sum)

    except ValueError:
        print("please enter the valid number.")    

if __name__ == "__main__":
    sum()        