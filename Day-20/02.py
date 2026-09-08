# Generate Fibonacci numbers up to N terms

def print_fibonacci():

    try:
        n= int(input("ENTER YOUR NUMBER HERE.: "))

        for i in range(0,n):

            def fibonacci(n):
                if n == 1 :
                    return 1
                if n == 0:
                    return 0
                
                return fibonacci(n-1) + fibonacci(n-2)

            print(fibonacci(i))


    except ValueError:
        print("Invalid input! Please enter an Integer.")
    

if __name__ == "__main__":
    (print_fibonacci())              