#  Check whether a number is an Armstrong number.

def armstrong_number():

    try:
        num = int(input("ENTER THE NUMBERE HERE.: "))
        n = num
        total = 0

        while n > 0:
            last_digit = n % 10
            total = total + (last_digit ** (len(str(num))))
            n = n // 10

        if (num == total)   :
            print(f"{num} is a armstrong number")
        else:
            print("number is not a armstrong number..")     


    except ValueError:
        print("Please enter the valid integer .")

print(armstrong_number())                   

