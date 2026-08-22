# 4.	Calculate the absolute value of a number without using abs().

def calculate_absolute():
    try:
        n = int(input("Enter teh number here .: "))

        if n < 0:
            print(f"The absolute valuse is {n * (-1)}")

        else:
            print(f"The absolute valuse is {n}")    

    except ValueError:
        print("Please enter valid numbers.")


if __name__ == "__main__":
    calculate_absolute()