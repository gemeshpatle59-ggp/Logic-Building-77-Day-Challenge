#  Find the number of trailing zeros in N! using an efficient mathematical method

def trailingzero():
    try:
        n = int(input("ENTER YOUR NUMBER HERE.: "))
        fact = 1

        for i in range(1,n+1):
            fact *= i

        zero = 0

        while fact > 0:
            if fact % 10 == 0:
                zero += 1
                fact = fact//10
            else:
                break

        print(zero)

    except ValueError:
        print("Invalid input! Please enter an Integer.")
    

if __name__ == "__main__":
    trailingzero()              