# Check whether a number is perfect.

def perfect_number():

    total = 0

    try:
        n = int(input("ENTER THE NUMBERE HERE.: "))

        for num in range(1,(n//2) +1):
            if n % num == 0:
                total += num
        if total == n:
            print(f"{n} is a perfect number.")

        else:
            print(f"{n} is not a perfect number..")    

    except ValueError:
        print("Please enter the valid integer .")

perfect_number()                   

