# Check whether a number is a happy number.

def check_happy():
    try:
        num = int(input("ENTER YOUR NUMBER HERE.: "))

        def number(n):
            seen = set()
            while n != 1:

                if n in seen:
                    return False

                seen.add(n)
                
                total = 0
                while n > 0:
                    last_digit = n % 10
                    total = total + (last_digit ** 2)
                    n = n// 10
                n = total

            return True   

        return number(num)


    except ValueError:
        print("Invalid input! Please enter an Integer.")
    

if __name__ == "__main__":
    print(check_happy())                