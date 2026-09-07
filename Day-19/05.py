#  Find the digital root of a number.

def find_digital_root():

    try:
        num = int(input("ENTER YOUR 1st NUMBER HERE.: "))
        
        def root(n):
            if n  < 10:
                return n

            total = 0

            while n > 0:
                total += n % 10
                n //= 10

            return root(total)

        return root(num)
        
    except ValueError:
        print("Invalid input! Please enter an Integer.")
    

if __name__ == "__main__":
    print(find_digital_root())              