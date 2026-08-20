# 2.	Check whether a number is even or odd

def even_odd():

    while True:

        try:
            n = int(input("ENTER THE NUMBER HERE.: "))

            if n % 2 == 0:
                print("The number is Even.")
                break

            else:
                print("The number is Odd")    
                break

        except ValueError:
            print("Please enter the number only.")    


if __name__ == "__main__":
    even_odd()           