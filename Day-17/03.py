#  Print all strong numbers in a range.


def strong_number():
    try:
        nums = int(input("ENTER THE NUMBER HERE.: "))

        factorial = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

        for num in range(nums+1):

            total = 0
            n = num

            while n > 0:
                digit = n % 10
                total += factorial[digit]
                n //= 10

            if total == num:
                print(num)
    
    except ValueError:
        print("Please enter the integer value.")


strong_number()
