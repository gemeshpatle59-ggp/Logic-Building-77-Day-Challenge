#  Count the factors of a number.

def count_factor():

    count = 0

    try:
        n = int(input("ENTER THE NUMBERE HERE.: "))

        for num in range(1,(n//2) +1):
            if n % num == 0:
                count += 1

        return count 

    except ValueError:
        print("Please enter the valid integer .")

print(count_factor())                   

