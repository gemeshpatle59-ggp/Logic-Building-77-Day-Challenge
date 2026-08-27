#  Keep taking numbers until 0 is entered and find their sum.

def calculate_sum():
    total = 0

    while True:
        try:
            num = int(input("Enter a number: "))
        except ValueError:
            print("Invalid input! Please enter an integer.")
            continue

        if num == 0:
            return total

        total += num


if __name__ == "__main__":
    print("Total:", calculate_sum())