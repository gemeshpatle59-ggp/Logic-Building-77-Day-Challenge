#  Find the sum of the first N Fibonacci numbers.

def add_fibbonacii():

    try:
        n= int(input("ENTER YOUR NUMBER HERE.: "))
        a = 0
        b = 1
        total = 0

        for _ in range(n):
            total += a
            a ,b = b , a+b

        print(f"sum of fibonacci number is {total}")

    except ValueError:
        print("Invalid input! Please enter an Integer.")
    

if __name__ == "__main__":
    (add_fibbonacii())              