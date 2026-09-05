# Check whether a number is a strong number

def strong_number():
    try:
        num = int(input("ENTER THE NUMBER HERE.: "))

        n = len(str(num))
        m = str(num)
        total = 0

        for i in range(n):
            fact = 1
            for j in range(1,int(m[i])+1):
                fact *= j

            total = fact + total     

        if total == num:
            print("given number is strong number")
        else:
            print("given number is not a strong number.")            

    except ValueError:
        print("Please enter the integer value.")         

strong_number()
