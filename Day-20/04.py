#  Check whether a number belongs to the Fibonacci sequence.

def print_fibonacci():

    try:
        n = int(input("Enter number: "))

        a = 0
        b = 1

        while a <= n:
            if a == n:
                print("Fibonacci number")
                break

            a, b = b, a + b
        else:
            print("Not a Fibonacci number")
            
    except ValueError:
        print("Invalid input! Please enter an Integer.")
    

if __name__ == "__main__":
    print(print_fibonacci())              