#  Print all perfect numbers in a range.


def perfect_number():

    try:
        n = int(input("ENTER THE RANGE OF NUMBERE HERE.: "))

        for j in range(1,n):
            total = 0
            
            for num in range(1,(j//2) +1):
                if j % num == 0:
                    total += num
            if total == j:
                print(f"{j} ")
    

    except ValueError:
        print("Please enter the valid integer .")

perfect_number()                   

