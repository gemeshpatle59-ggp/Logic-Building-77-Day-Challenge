#  Keep taking numbers until a negative number is entered and count valid inputs

def Calculate_valid_input():

    count = 0

    while True:

        try:
            nums = int(input("Enter the number here.."))
        except ValueError:
            print("Invalid input! Please enter an Integer.")
            continue

        if nums < 0:
            break

        count += 1

    return count


if __name__ == "__main__":
    print("valid inputs :" ,Calculate_valid_input())        