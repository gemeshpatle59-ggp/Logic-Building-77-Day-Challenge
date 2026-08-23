# 2.	Check whether two numbers have the same last digit

def check_lastdigit():

    try:
        n = int(input("ENTER THE 1ST NUMBER HERE.: "))
        m = int(input("ENTER THE 2ND NUMBER HERE.: "))

        if n % 10 == m % 10:
            print("Yes the two number has same last digit.")

        else:
            print("No the two number does not have same last digit.")    

    except ValueError:
        print("Please enter the valid number in input.")

if __name__ == "__main__":
    check_lastdigit()               