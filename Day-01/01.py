# 1.	Check whether a number is positive, negative, or zero

def number_check():

    while True:

        try:
            n = int(input("ENTER THE NUMBER HERE.: "))

            if n > 0:
                print(f"number is positive")
                break

            elif n < 0:
                print("number is negative")
                break

            else:
                print("number is zero .")
                break

        except ValueError:
            print("please enter the number olny .")                  

if __name__ == "__main__":
    number_check()