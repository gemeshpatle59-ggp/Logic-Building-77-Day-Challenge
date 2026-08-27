#  Print all numbers between A and B satisfying a given divisibility condition.

def divisibility_condition():

    try:
        a = int(input("ENTER THE FIRST NUMBER HERE.: "))
        b = int(input("ENTER THE SECOND NUMBER HERE.: "))
        divisible = int(input("ENTER A NUMBER WANT TO DIVISIBLE BY.: "))
    except ValueError:
        print("Invalid input! Please enter an Integer.")
        return
    if divisible == 0:
        print("Divide by Zero cannot possible.")
        return

    if a <= b :
        for i in range(a,b+1):
            if i % divisible == 0:
                print(i)
        
    else:
        print("FIRST NUMBER CANNOT BE GREATER THAN SECOND NUMBER..")         

if __name__ == "__main__":
    divisibility_condition()        