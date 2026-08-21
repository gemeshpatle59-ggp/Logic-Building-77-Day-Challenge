# 2.	Check whether a year is a leap year using the complete Gregorian rule.

def leap_year():
    try:
        n = int(input("ENTER THE YEAR HERE.: "))

        if n % 400 == 0 or (n % 4 == 0 and n % 100 != 0):
            print(f"{n} is a leap year.")

        else:
            print(f"{n} is not a leap year.")

    except ValueError:
        print("Please enyter the valid year..")            

if __name__ == "__main__":
    leap_year()