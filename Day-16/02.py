#  Find the sum of proper divisors.

def divisior_sum():

    total = 0

    try:
        n = int(input("ENTER THE NUMBERE HERE.: "))

        for num in range(1,(n//2) +1):
            if n % num == 0:
                total += num

        print(f"The sum of prp\oper divisior is {total}")

    except ValueError:
        print("Please enter the valid integer .")

divisior_sum()                   

