#  Find the Nth Fibonacci number.

def find_nth_fibonacci():

    try:
        n= int(input("ENTER YOUR NUMBER HERE.: "))

        def fibonacci(n):
            if n == 1 :
                return 1
            if n == 0:
                return 0
            
            return fibonacci(n-1) + fibonacci(n-2)

        return fibonacci(n)


    except ValueError:
        print("Invalid input! Please enter an Integer.")
    

if __name__ == "__main__":
    print(find_nth_fibonacci())              