#  Check whether a number is a Harshad/Niven number

def check_harshad():
    try:
        num = int(input("ENTER YOUR NUMBER HERE.: "))
    except ValueError:
        print("Invalid input! Please enter an Integer.")
        return

    total = 0

    if num <= 0:
        print("Zero or negative number is not harshad number..")
        return

    for i in str(num):
        total += int(i)

    if num % total == 0:
        print(f"{num} is a harshad number..")

    else:
        print(f"{num} is not a harshad number..")

if __name__ == "__main__":
    check_harshad()                