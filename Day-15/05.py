#  Find all factors of a number

def all_factor():
    try:
        n = int(input("ENTER THE NUMBERE HERE.: "))

        for num in range(1,(n//2) +1):
            if n % num == 0:
                print(num)

        print(n) 

    except ValueError:
        print("Please enter the valid integer .")

all_factor()                   

